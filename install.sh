#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

if [ "$(id -u)" -ne 0 ]; then
  echo "Please run this installer as root (sudo ./install.sh)"
  exit 1
fi

REAL_USER=${SUDO_USER:-$USER}

echo "Running setup for user: $REAL_USER"

if [ ! -d "venv" ]; then
  echo "Creating new virtual environment..."
  sudo -u "$REAL_USER" python3 -m venv "$DIR/venv"
else
  echo "Virtual environment already exists. Skipping creation."
fi

sudo -u "$REAL_USER" "$DIR/venv/bin/python3" -m pip install -r requirements.txt

RUN_SCRIPT="$DIR/run.sh"
chmod +x "$RUN_SCRIPT"

# --- Install sensor read crontab ---
CRON_PATH="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
CRON_JOB="* * * * * $RUN_SCRIPT >> $DIR/cron_output.log 2>&1"

TMP_CRON=$(mktemp)
sudo -u "$REAL_USER" crontab -l 2>/dev/null | sudo -u "$REAL_USER" tee "$TMP_CRON" > /dev/null

if ! grep -q "PATH=" "$TMP_CRON"; then
  CRON_CONTENT=$(cat "$TMP_CRON")
  echo -e "$CRON_PATH\n$CRON_CONTENT" | sudo -u "$REAL_USER" tee "$TMP_CRON" > /dev/null
fi

if ! grep -q "$RUN_SCRIPT" "$TMP_CRON"; then
  echo "$CRON_JOB" >> "$TMP_CRON"
  sudo -u "$REAL_USER" crontab "$TMP_CRON"
  echo "Successfully installed cron job!"
else
  echo "Cron job configuration already exists. Skipping."
fi

rm "$TMP_CRON"

# --- UDEV RULE SETUP ---
UDEV_RULE_PATH="/etc/udev/rules.d/99-usb-sync.rules"

echo "Installing udev rule (Requires sudo access)..."

# Explicitly using sudo to write to system directories securely
sudo tee "$UDEV_RULE_PATH" > /dev/null << EOF
ACTION=="add", SUBSYSTEM=="block", ENV{ID_USB_DRIVER}=="usb-storage", RUN+="$RUN_SCRIPT sync &"
EOF

# Reload udev system configurations
echo "Reloading udev rules..."
sudo udevadm control --reload-rules
sudo udevadm trigger

echo "Installation complete!"
