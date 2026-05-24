#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

# 1. Enforce root execution to ensure udev rules can be safely removed
if [ "$(id -u)" -ne 0 ]; then
  echo "Please run this uninstaller as root (sudo ./uninstall.sh)"
  exit 1
fi

REAL_USER=${SUDO_USER:-$USER}
RUN_SCRIPT="$DIR/run.sh"

echo "Beginning uninstallation of PAC3220 Reader automation for user: $REAL_USER..."

# --- 1. Clean Up Crontab Settings ---
TMP_CRON=$(mktemp)

# FIXED: Read user's crontab into temporary file safely preserving permissions via tee
sudo -u "$REAL_USER" crontab -l 2>/dev/null | sudo -u "$REAL_USER" tee "$TMP_CRON" > /dev/null

if grep -q "$RUN_SCRIPT" "$TMP_CRON"; then
  echo "Removing cron job entry..."

  # Filter out the line containing our execution script path safely
  sed -i "\|$RUN_SCRIPT|d" "$TMP_CRON"

  # Check if the crontab is now empty or only contains our PATH declaration variable.
REMAINING_JOBS=$(grep -v -c -E "(^PATH=|^#|^$)" "$TMP_CRON")
  if [ "$REMAINING_JOBS" -eq 0 ]; then
    echo "No other cron tasks found. Cleaning up environment variables..."
    # Clear the file contents safely within the user scope
    echo -n "" | sudo -u "$REAL_USER" tee "$TMP_CRON" > /dev/null
  fi

  # Apply the updated changes back to the active user system crontab safely
  if [ -s "$TMP_CRON" ]; then
    sudo -u "$REAL_USER" crontab "$TMP_CRON"
  else
    # If the file ended up completely empty, purge the crontab layout cleanly
    sudo -u "$REAL_USER" crontab -r 2>/dev/null
  fi
  echo "Successfully removed cron configurations!"
else
  echo "No active cron job found for $REAL_USER. Skipping."
fi

rm "$TMP_CRON"

# --- 2. Clean Up Local Virtual Environment ---
# FIXED: Using fully qualified absolute variable paths
if [ -d "$DIR/venv" ]; then
  echo "Removing Python virtual environment ($DIR/venv)..."
  rm -rf "$DIR/venv"
  echo "Virtual environment successfully deleted."
else
  echo "No virtual environment found. Skipping."
fi

# --- 3. Remove UDEV rule ---
UDEV_RULE_PATH="/etc/udev/rules.d/99-usb-sync.rules"
if [ -f "$UDEV_RULE_PATH" ]; then
  echo "Removing system udev rule..."
  rm "$UDEV_RULE_PATH"

  # Reload udev system configurations to make sure the change takes effect immediately
  echo "Reloading udev rules..."
  udevadm control --reload-rules
  udevadm trigger
  echo "Udev rule successfully uninstalled."
else
  echo "No active udev rule found. Skipping."
fi

echo "Uninstallation complete! (Your local log files and source files have been preserved)."