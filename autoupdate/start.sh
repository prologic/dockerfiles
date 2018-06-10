#!/bin/sh

MSGBUS_URI="${MSGBUS_URI:-https://msgbus.mills.io}"
MSGBUS_TOPIC="${MSGBUS_TOPIC:-ci.mills.io}"

exec msgbus -d sub "${MSGBUS_TOPIC}" /usr/local/bin/autoupdate.sh "${@}"
