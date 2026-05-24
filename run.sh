#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

CURRENT_UID=$(id -u)

if [ "$CURRENT_UID" -eq 0 ]; then
    exec sudo -u '#1000' -g '#1000' $DIR/venv/bin/python $DIR/main.py "$@"

elif [ "$CURRENT_UID" -eq 1000 ]; then
    exec $DIR/venv/bin/python $DIR/main.py "$@"

else
    echo "Error: This script must be run by root or user 1000." >&2
    exit 1
fi