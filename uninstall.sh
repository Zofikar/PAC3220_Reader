#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

RUN_SCRIPT="$DIR/run.sh"

echo "Beginning uninstallation of PAC3220 Reader automation..."

# --- 1. Clean Up Crontab Settings ---
TMP_CRON=$(mktemp)
crontab -l > "$TMP_CRON" 2>/dev/null

if grep -q "$RUN_SCRIPT" "$TMP_CRON"; then
  echo "Removing cron job entry..."
  # Filter out the line containing our execution script path
  sed -i "\|$RUN_SCRIPT|d" "$TMP_CRON"

  # Check if the crontab is now empty or only contains our PATH declaration variable.
  # If it only contains our PATH and nothing else, clean up the PATH declaration too.
  REMAINING_JOBS=$(grep -v -E "(^PATH=|^#|^$)" "$TMP_CRON" | wc -l)
  if [ "$REMAINING_JOBS" -eq 0 ]; then
    echo "No other cron tasks found. Cleaning up environment variables..."
    > "$TMP_CRON"
  fi

  # Apply the updated changes back to the active user system crontab
  if [ -s "$TMP_CRON" ]; then
    crontab "$TMP_CRON"
  else
    # If the file ended up completely empty, purge the crontab layout cleanly
    crontab -r 2>/dev/null
  fi
  echo "Successfully removed cron configurations!"
else
  echo "No active cron job found. Skipping."
fi

rm "$TMP_CRON"

# --- 2. Clean Up Local Virtual Environment ---
if [ -d "venv" ]; then
  echo "Removing Python virtual environment (venv/)..."
  rm -rf venv
  echo "Virtual environment successfully deleted."
else
  echo "No virtual environment found. Skipping."
fi

echo "Uninstallation complete! (Your local log files and source files have been preserved)."

# --- 3. Unmount usb ---
sudo unmount ./usb

echo "Uninstallation complete! (Your local log files and source files have been preserved)."