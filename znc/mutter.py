#
#  mutter.py
#  Mutter
#
#   /$$      /$$             /$$     /$$
#  | $$$    /$$$            | $$    | $$
#  | $$$$  /$$$$ /$$   /$$ /$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$
#  | $$ $$/$$ $$| $$  | $$|_  $$_/|_  $$_/   /$$__  $$ /$$__  $$
#  | $$  $$$| $$| $$  | $$  | $$    | $$    | $$$$$$$$| $$  \__/
#  | $$\  $ | $$| $$  | $$  | $$ /$$| $$ /$$| $$_____/| $$
#  | $$ \/  | $$|  $$$$$$/  |  $$$$/|  $$$$/|  $$$$$$$| $$
#  |__/     |__/ \______/    \___/   \___/   \_______/|__/
#
#  Copyright 2016 Matthew Clough <support@mutterirc.com>
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

# CHANGES BY MUFFINMEDIC
# Add support for private messages and away_only
# (1) 'sendAll' parameter in 'handle_message' to bypass regex match (for private messages)
# (2) 'channel' parameter in 'handle_message' for passing channel notification for pings in channels (blank for private messages)
# (3) 'IsIRCAway()' in 'handle_message' to only send notification if user marked away
# (4) Add network name to notification
# (5) Bold formatted title

# Changes by James Mills (prologic)
# (1) Disable silly ISIRCAway() logic


import json
import os.path
import re
import requests
import znc

MUTTER_PUSH_IRCV3_CAPABILITY = "mutterirc.com/push"
MUTTER_SERVER_URL = "https://api.mutterirc.com:8100"
MUTTER_STATE_FILE = "mutter.json"
MUTTER_USER_AGENT = "MutterZNC/1.0"

class mutter(znc.Module):

    module_types = [znc.CModInfo.GlobalModule]

    description = "Mutter push notification module"

    networks = {}

    stripControlCodesRegex = re.compile("\x1d|\x1f|\x0f|\x02|\x03(?:\d{1,2}(?:,\d{1,2})?)?", re.UNICODE)

    def mutter_state_file(self):
        return "{0}/{1}".format(self.GetSavePath(), MUTTER_STATE_FILE)

    def network_identifier(self):
        return "{0}/{1}".format(self.GetNetwork().GetUser().GetUserName(), self.GetNetwork().GetName())

    def handle_user_raw(self, line):
        tokens = str(line).split()
        network = self.network_identifier()
        if (len(tokens) == 0) or (not tokens[0].lower() == "mutter"):
            return znc.CONTINUE
        if len(tokens) > 2:
            token = tokens[2]
            command = tokens[1].lower()
            if command == "begin":
                if network not in self.networks:
                    self.networks[network] = {}
                if token not in self.networks[network]:
                    self.networks[network][token] = {}
                self.networks[network][token].update({ "active" : False })
                self.networks[network][token].update({ "keywords" : [] })
                self.networks[network][token].update({ "blocks" : [] })
            if command == "version" and len(tokens) == 4:
                self.networks[network][token].update({ "version" : tokens[3]})
            if command == "keyword" and len(tokens) > 3:
                keyword = str(line).split(':',1)[1]
                self.networks[network][token]["keywords"].append(keyword)
            if command == "block" and len(tokens) == 4:
                block = tokens[3].replace("*", "(.*?)")
                self.networks[network][token]["blocks"].append(block)
            if command == "end":
                self.networks[network][token].update({ "active" : True })
                with open(self.mutter_state_file(), 'w') as outfile:
                    json.dump(self.networks, outfile, sort_keys = True, indent = 4)
        return znc.HALT

    def blocked_nick(self, nick):
        network = self.network_identifier()
        if network in self.networks:
            for token in self.networks[network].keys():
                if self.networks[network][token]["active"] == True:
                    for block in self.networks[network][token]["blocks"]:
                        pattern = re.compile(block)
                        if pattern.match(nick.GetNickMask()):
                            return True
        return False

    # Added channel and sendAll parameters
    def handle_message(self, channel, nick, message, sendAll):
        if not self.blocked_nick(nick):
            network = self.network_identifier()
            if network in self.networks:
                for token in self.networks[network].keys():
                    if self.networks[network][token]["active"] == True:
                        for keyword in self.networks[network][token]["keywords"]:
                            line = self.stripControlCodesRegex.sub('', message.s)
                            # Added sendAll argument
                            if sendAll or re.search(r'(?:[\s]|[^\w]|^)({0})(?=[\s]|[^\w]|$)'.format(re.escape(keyword)), line, re.IGNORECASE):
                                version = self.networks[network][token]["version"]
                                # Split title and body for formatting
                                if channel:
                                    title = "{} ({} @ {})".format( nick.GetNick(), channel.GetName(), self.GetNetwork().GetName())
                                else:
                                    title = "{} ({})".format(nick.GetNick(), self.GetNetwork().GetName())
                                body = "{}".format(line)
                                self.send_notification(version, token, title, body)
                                break
        return znc.CONTINUE

    # Split "line" into "title" and "body" for APNS formatting
    def send_notification(self, version, token, title, body):
        session = requests.Session()
        session.headers['User-Agent'] = MUTTER_USER_AGENT
        alert = { 'title' : title, 'body' : body }
        payload = { 'version' : version, 'token' : token, 'alert' : alert }
        try:
            response = session.post(MUTTER_SERVER_URL, verify=True, timeout=30, data=json.dumps(payload), headers={"content-type": "text/javascript"})
            data = response.json()
            if 'error' in data and 'code' in data['error']:
                if data['error']['code'] == "200":
                    expired_token = data['error']['token']
                    self.remove_token_from_networks(expired_token)
        except requests.exceptions.RequestException as e:
            self.PutModule("Error: {}".format(e))
            
    def remove_token_from_networks(self, token):
        for network in self.networks.keys():
            if token in self.networks[network]:
                del self.networks[network][token]
        with open(self.mutter_state_file(), 'w') as outfile:
            json.dump(self.networks, outfile, sort_keys = True, indent = 2)

    def OnLoad(self, args, message):
        if os.path.exists(self.mutter_state_file()):
            with open(self.mutter_state_file()) as data_file:
                self.networks = json.load(data_file)
        return True

    def OnClientCapLs(self, pClient, ssCaps):
        ssCaps.insert(MUTTER_PUSH_IRCV3_CAPABILITY)

    def IsClientCapSupported(self, pClient, sCap, bState):
        return True if sCap == MUTTER_PUSH_IRCV3_CAPABILITY else False

    def OnUserRaw(self, line):
        return self.handle_user_raw(line)

    # Added channel parameter for channel and 'False' for sendAll in message handler
    def OnChanMsg(self, nick, channel, message):
        return self.handle_message(channel, nick, message, False)

    # Added channel parameter for channel and 'False' for sendAll in message handler
    def OnChanAction(self, nick, channel, message):
        return self.handle_message(channel, nick, message, False)

    # Added channel parameter for channel and 'False' for sendAll in message handler
    def OnChanNotice(self, nick, channel, message):
        return self.handle_message(channel, nick, message, False)

    # Added 'none' for channel to message handler and 'True' for sendAll
    def OnPrivMsg(self, nick, message):
        return self.handle_message(None, nick, message, True)

    # Added 'none' for channel to message handler and 'True' for sendAll
    def OnPrivAction(self, nick, message):
        return self.handle_message(None, nick, message, True)
        
    # Added 'none' for channel to message handler and 'True' for sendAll
    def OnPrivNotice(self, nick, message):
        if not (message.s).startswith("***"):
            return self.handle_message(None, nick, message, True)
