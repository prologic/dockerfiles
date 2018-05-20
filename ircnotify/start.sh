#!/bin/sh

export JQ_TEMPLATE="${JQ_TEMPLATE:-${1}}"

MSGBUS_URI="${MSGBUS_URI:-https://msgbus.mills.io}"
MSGBUS_TOPIC="${MSGBUS_TOPIC:-hello}"

exec msgbus -d sub "${MSGBUS_TOPIC}" /usr/local/bin/ircnotify.sh
