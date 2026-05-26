#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RUN_SCRIPT="$DIR/run.sh"
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


chmod +x "$RUN_SCRIPT"

# --- Install sensor read crontab ---
CRON_PATH="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
CRON_JOB="0 * * * * $RUN_SCRIPT >> $DIR/cron_output.log 2>&1"

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
USB_SYNC_D="/etc/systemd/system/usb-sync@.service"
SUDOERS_PATH="/etc/sudoers.d/usb-sync-mount"

echo "Installing systemd service and udev rule..."

# Create systemd service
sudo tee "$USB_SYNC_D" > /dev/null << EOF
[Unit]
Description=Sync USB partition %I

[Service]
Type=simple
ExecStart=$RUN_SCRIPT --sync /dev/%I
EOF

# Explicitly using sudo to write to system directories securely
sudo tee "$UDEV_RULE_PATH" > /dev/null << 'EOF'
ACTION=="add", SUBSYSTEM=="block", ENV{DEVTYPE}=="partition", ENV{ID_USB_DRIVER}=="usb-storage", TAG+="systemd", ENV{SYSTEMD_WANTS}="usb-sync@%k.service"
EOF

echo "Configuring passwordless sudo permissions for mount/umount..."
sudo tee "$SUDOERS_PATH" > /dev/null << 'EOF'
# Allow user with UID 1000 to use mount and umount without a password
#1000 ALL=(ALL) NOPASSWD: /usr/bin/mount, /usr/bin/umount
EOF

# Reload udev system configurations
echo "Reloading udev rules..."
sudo systemctl daemon-reload
sudo udevadm control --reload-rules

echo "Installation complete!"
