#!/usr/bin/env python3
import argparse
import logging
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import yaml

from Protocol.Protocol import DictWrapper
from Storage import FsLockStorage, FileLock
from Storage.Writter import CsvWriter, JsonWriter

BASE = Path(__file__).parent.absolute()

logfile = BASE / "log.txt"
logfile.parent.mkdir(parents=True, exist_ok=True)
USB_MOUNT_POINT = BASE / "usb"
logging.basicConfig(
    filename=logfile,
    filemode="a",
    format="[%(asctime)s] %(name)s - %(levelname)s - %(funcName)s(%(lineno)d) - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

config_file = BASE / "config.yaml"
config = {}
try:
    with open(config_file) as f:
        config = yaml.safe_load(f)
except FileNotFoundError:
    logger.warning(f"Config {config_file} not found.")

FILENAME = "data"
writer_type = config.get("writer", "json")
if writer_type == "csv":
    writer = CsvWriter()
    FILENAME += '.csv'
else:
    writer = JsonWriter()
    FILENAME += '.json'

FS_STORAGE_PATH = BASE / "storage" / FILENAME


def get_usb_device() -> Path:
    by_path_dir = Path("/dev/disk/by-path")

    if by_path_dir.is_dir():
        for link in by_path_dir.iterdir():
            if "-usb-" in link.name and link.name.endswith("-part1"):
                try:
                    real_device_path = link.resolve(strict=True)
                    return real_device_path
                except FileNotFoundError:
                    continue

    fallback_path = Path("/dev/sda1")
    if fallback_path.exists():
        return fallback_path

    raise FileNotFoundError("Hotswap Failure: No active USB storage partition detected on the hub.")

def main():

    from Reader import Pac3220ModbusReader, Pac3220ModbusFactory

    storage_engine = FsLockStorage[DictWrapper](target_file_path=FS_STORAGE_PATH, storage_label="FS", writer=writer)

    device_ip = config.get("device_ip", "127.0.0.1")
    device_port = int(config.get("device_port", 5020))
    device_id = int(config.get("device_id", 1))

    factory = Pac3220ModbusFactory([int(d) for d in config["registers"]])

    reader = Pac3220ModbusReader(device_ip, device_port, device_id, factory, storage_engine)

    try:
        logger.info(f"Attempting to read data from device {device_ip}:{device_port} at id {device_id}...")
        reader.read_and_store()
        logger.info("Data read successfully.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


def sync():
    lockfile = FS_STORAGE_PATH.with_name(FS_STORAGE_PATH.name + ".lock")
    lockfile.parent.mkdir(parents=True, exist_ok=True)
    device = get_usb_device()
    mount_point = FS_STORAGE_PATH.parent / "usbmnt"

    subprocess.run(
        ["sudo", "mount", "-o", "umask=000,sync", str(device), str(mount_point)],
        check=True, capture_output=True
    )

    mounted_file = mount_point / datetime.now().strftime("%d.%m.%Y %H.%M.%S") / FILENAME
    mounted_file.parent.mkdir(parents=True, exist_ok=True)
    with FileLock(lockfile):
        shutil.move(FS_STORAGE_PATH, mounted_file)

    subprocess.run(
        ["sudo", "umount", str(mount_point)],
        check=True, capture_output=True
    )


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("sync")

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    if args.sync:
        sync()
        sys.exit(0)
    main()
