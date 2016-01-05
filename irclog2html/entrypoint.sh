#!/bin/bash

export PATH="$HOME/bin:$PATH"

for dir in *; do
    if [ -d $dir ]; then
        logs2html -t "IRC Logs for $dir " -p "IRC Logs for $dir " $dir
    fi
done
