#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

# Ensure the script is run as root
if [ "$(id -u)" -ne 0 ]; then
  echo "Please run this uninstaller as root (sudo ./uninstall.sh)"
  exit 1
fi

REAL_USER=${SUDO_USER:-$USER}
echo "Running uninstaller for user: $REAL_USER"

# --- 1. REMOVE CRON JOB ---
echo "Removing cron job..."
RUN_SCRIPT="$DIR/run.sh"
EXISTING_CRON=$(sudo -u "$REAL_USER" crontab -l 2>/dev/null)

if [ -n "$EXISTING_CRON" ]; then
  # Filter out the specific cron job line
  NEW_CRON=$(echo "$EXISTING_CRON" | grep -v -F "$RUN_SCRIPT")

  # Check if only the PATH variable is left. If so, clear the crontab entirely.
  # Otherwise, update the crontab with the remaining jobs.
  CLEANED_CRON=$(echo "$NEW_CRON" | grep -v "^PATH=" | tr -d '[:space:]')

  if [ -z "$CLEANED_CRON" ]; then
    sudo -u "$REAL_USER" crontab -r 2>/dev/null
    echo "Crontab cleared successfully."
  else
    echo "$NEW_CRON" | sudo -u "$REAL_USER" crontab -
    echo "Cron job removed successfully."
  fi
else
  echo "No crontab found for user $REAL_USER. Skipping."
fi

# --- 2. REMOVE SYSTEMD AND UDEV CONFIGURATIONS ---
UDEV_RULE_PATH="/etc/udev/rules.d/99-usb-sync.rules"
USB_SYNC_D="/etc/systemd/system/usb-sync@.service"
SUDOERS_PATH="/etc/sudoers.d/usb-sync-mount"

echo "Removing systemd service, udev rules, and sudoers config..."

[ -f "$USB_SYNC_D" ] && rm -f "$USB_SYNC_D"
[ -f "$UDEV_RULE_PATH" ] && rm -f "$UDEV_RULE_PATH"
[ -f "$SUDOERS_PATH" ] && rm -f "$SUDOERS_PATH"

# Reload system configurations to apply changes
echo "Reloading system daemons..."
systemctl daemon-reload
udevadm control --reload-rules

# --- 3. REMOVE VIRTUAL ENVIRONMENT & LOGS ---
if [ -d "venv" ]; then
  echo "Removing virtual environment..."
  rm -rf "venv"
else
  echo "No virtual environment found. Skipping."
fi

if [ -f "cron_output.log" ]; then
  echo "Removing cron log file..."
  rm -f "cron_output.log"
fi

echo "Uninstallation complete!"