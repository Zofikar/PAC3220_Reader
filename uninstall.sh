#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

if [ "$(id -u)" -ne 0 ]; then
  echo "Please run this uninstaller as root (sudo ./uninstall.sh)"
  exit 1
fi

REAL_USER=${SUDO_USER:-$USER}
RUN_SCRIPT="$DIR/run.sh"

echo "Beginning uninstallation of PAC3220 Reader automation for user: $REAL_USER..."

# --- 1. Clean Up Crontab Settings ---
echo "Checking cron jobs for user: $REAL_USER..."

EXISTING_CRON=$(sudo -u "$REAL_USER" crontab -l 2>/dev/null)

if echo "$EXISTING_CRON" | grep -q "$RUN_SCRIPT"; then
  echo "Removing cron job entry..."

  UPDATED_CRON=$(echo "$EXISTING_CRON" | grep -v "$RUN_SCRIPT")

  REMAINING_JOBS=$(echo "$UPDATED_CRON" | grep -v -c -E "(^PATH=|^#|^$)")

  if [ "$REMAINING_JOBS" -eq 0 ]; then
    echo "No other cron tasks found. Purging crontab entirely..."
    sudo -u "$REAL_USER" crontab -r 2>/dev/null
  else
    echo "$UPDATED_CRON" | sudo -u "$REAL_USER" crontab -
  fi

  echo "Successfully removed cron configurations!"
else
  echo "No active cron job found for $REAL_USER. Skipping."
fi

# --- 2. Clean Up Local Virtual Environment ---
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