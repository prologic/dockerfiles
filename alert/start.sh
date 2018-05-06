#!/bin/sh

MSGBUS_URI="${MSGBUS_URI:-https://msgbus.mills.io}"
MSGBUS_TOPIC="${MSGBUS_TOPIC:-alerts}"

exec msgbus -d sub "${MSGBUS_TOPIC}" /usr/local/bin/alert.sh
