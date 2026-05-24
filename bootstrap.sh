#!/bin/bash

if [ "$(id -u)" -ne 0 ]; then
  echo "Please run this bootstrap as root"
  exit 1
fi

TARGET_USER=$(id -nu 1000 2>/dev/null)
TARGET_HOME=$(getent passwd 1000 | cut -d: -f6)

if [ -z "$TARGET_USER" ] || [ -z "$TARGET_HOME" ]; then
  echo "Error: Could not find a regular user with UID 1000."
  exit 1
fi

echo "Targeting user: $TARGET_USER ($TARGET_HOME)"

# --- ensure git ---

if ! command -v git &> /dev/null; then
  echo "Git is not installed. Attempting to install it now..."

  apt-get update && apt-get install -y git

  if ! command -v git &> /dev/null; then
    echo "Error: Failed to install Git. Please install it manually and try again."
    exit 1
  fi
  echo "Git installed successfully."
fi

# --- clone the repo ---

echo "Cloning repository into $TARGET_HOME..."
sudo -u "$TARGET_USER" git clone https://github.com/Zofikar/PAC3220_Reader.git "$TARGET_HOME/PAC3220_Reader"

if [ $? -ne 0 ]; then
  echo "Git clone failed"
  exit 1
fi

cd "$TARGET_HOME/PAC3220_Reader" || { echo "Can not get into repo dir"; exit 1; }

chmod +x install.sh
./install.sh


# --- Static ip on eth0 ---
INTERFACE="eth0"
CONNECTION_NAME="eth0-isolated"
IP_ADDRESS="192.168.1.99/24"

echo "Configuring static IP on $INTERFACE for an isolated network..."

nmcli connection delete "$CONNECTION_NAME" &>/dev/null || true
nmcli connection delete "$INTERFACE" &>/dev/null || true

nmcli connection add type ethernet con-name "$CONNECTION_NAME" ifname "$INTERFACE" ip4 "$IP_ADDRESS"

nmcli connection modify "$CONNECTION_NAME" ipv4.method manual

nmcli connection modify "$CONNECTION_NAME" ipv4.never-default yes

echo "Bringing up the connection..."
nmcli connection up "$CONNECTION_NAME"

echo "Configuration complete. $INTERFACE is now set to $IP_ADDRESS (Isolated)."