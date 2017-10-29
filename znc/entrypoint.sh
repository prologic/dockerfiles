#!/bin/sh

# Options.
DATADIR="/data"

# Create default configs if it doesn't exist
if [ ! -d "${DATADIR}/configs" ]; then
  cp -r /usr/src/configs "${DATADIR}/configs"
fi

# Create default modules if it doesn't exist
if [ ! -d "${DATADIR}/modules" ]; then
  cp -r /usr/src/znc/modules "${DATADIR}/modules"
fi

chown -R znc:znc "$DATADIR"

# Start ZNC.
exec su -s '/bin/sh' -c "znc --foreground --datadir=\"$DATADIR\" $@" znc
