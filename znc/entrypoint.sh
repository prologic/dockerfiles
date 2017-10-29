#!/bin/sh

# Options.
DATADIR="/data"

# Create default config if it doesn't exist
if [ ! -f "${DATADIR}/configs/znc.conf" ]; then
  mkdir -p "${DATADIR}/configs"
  cp /znc.conf "${DATADIR}/configs/znc.conf"
fi

# Create default modules if it doesn't exist
if [ ! -d "${DATADIR}/modules" ]; then
  cp -r /usr/src/znc/modules "${DATADIR}/modules"
fi

chown -R znc:znc "$DATADIR"

# Start ZNC.
exec su -s '/bin/sh' -c "znc --foreground --datadir=\"$DATADIR\" $@" znc
