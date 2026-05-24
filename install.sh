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

echo "Installing cron job for user: $REAL_USER..."

EXISTING_CRON=$(sudo -u "$REAL_USER" crontab -l 2>/dev/null)

if echo "$EXISTING_CRON" | grep -q "$RUN_SCRIPT"; then
  echo "Cron job configuration already exists. Skipping."
else
  NEW_CRON=""

  if ! echo "$EXISTING_CRON" | grep -q "PATH="; then
    NEW_CRON="$CRON_PATH"$'\n'
  fi

  if [ -n "$EXISTING_CRON" ]; then
    NEW_CRON="$NEW_CRON$EXISTING_CRON"$'\n'
  fi
  NEW_CRON="$NEW_CRON$CRON_JOB"

  echo "$NEW_CRON" | sudo -u "$REAL_USER" crontab -
  echo "Successfully installed cron job!"
fi

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
