#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

if [ ! -d "venv" ]; then
  echo "Creating new virtual environment..."
  python3 -m venv venv
else
  echo "Virtual environment already exists. Skipping creation."
fi

venv/bin/python3 -m pip install -r requirements.txt

RUN_SCRIPT="$DIR/run.sh"
chmod +x "$RUN_SCRIPT"

CRON_PATH="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
CRON_JOB="*/15 * * * * ip route | grep -q default && $RUN_SCRIPT >> $DIR/cron_output.log 2>&1"

TMP_CRON=$(mktemp)
crontab -l > "$TMP_CRON" 2>/dev/null

if ! grep -q "PATH=" "$TMP_CRON"; then
  echo -e "$CRON_PATH\n$(cat "$TMP_CRON")" > "$TMP_CRON"
fi

if ! grep -q "$RUN_SCRIPT" "$TMP_CRON"; then
  echo "$CRON_JOB" >> "$TMP_CRON"
  crontab "$TMP_CRON"
  echo "Successfully installed cron job!"
else
  echo "Cron job configuration already exists. Skipping."
fi

rm "$TMP_CRON"