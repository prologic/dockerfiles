#!/bin/sh

IRC_NICK="${IRC_NICK:-alertmanager}"
IRC_HOST="${IRC_HOST:-irc.mills.io}"
IRC_PORT="${IRC_PORT:-6667}"
IRC_CHAN="${IRC_CHAN:-#alerts}"

payload="$(cat - | jq -r '.payload' | base64 -d)"

echo "${payload}" \
  | jq -r '.alerts[] | "ALERT: \(.labels.alertname) \(.status) - \(.annotations.summary)"' \
  | irccat -n "${IRC_NICK}" "${IRC_HOST}:${IRC_PORT}" "${IRC_CHAN}"
