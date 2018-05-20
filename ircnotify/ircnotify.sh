#!/bin/sh

JQ_TEMPLATE="${JQ_TEMPLATE:-"\"\\(.)\""}"

IRC_NICK="${IRC_NICK:-ircnotify}"
IRC_HOST="${IRC_HOST:-irc.mills.io}"
IRC_PORT="${IRC_PORT:-6667}"
IRC_CHAN="${IRC_CHAN:-#alerts}"

payload="$(cat - | jq -r '.payload' | base64 -d)"

echo "${payload}" \
  | jq -r "${JQ_TEMPLATE}" \
  | irccat -n "${IRC_NICK}" "${IRC_HOST}:${IRC_PORT}" "${IRC_CHAN}"
