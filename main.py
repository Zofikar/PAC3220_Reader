#!/usr/bin/env python3
import logging
from pathlib import Path

import yaml

from Protocol.Protocol import DictWrapper
from Storage.Writter import CsvWriter, JsonWriter

BASE = Path(__file__).parent.absolute()

logfile = BASE / "log.txt"
logfile.parent.mkdir(parents=True, exist_ok=True)
USB_MOUNT_POINT = BASE / "usb"
FILENAME = "Pac3220.csv"
FAILOVER_STORAGE_PATH = BASE / "failover" / FILENAME
logging.basicConfig(
    filename=logfile,
    filemode="a",
    format="[%(asctime)s] %(levelname)s - %(message)s",
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

from Reader import Pac3220ModbusReader, Pac3220ModbusFactory, ModbusTcpRegister
from Storage import FsStorage, MountStorage, TieredStorage


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


writer_type = config.get("writer", "json")
if writer_type == "csv":
    writer = CsvWriter()
else:
    writer = JsonWriter()

storage_engine = TieredStorage[DictWrapper]([
    MountStorage[DictWrapper](get_usb_device, USB_MOUNT_POINT, FILENAME, "USB", writer=writer),
    FsStorage[DictWrapper](target_file_path=FAILOVER_STORAGE_PATH, storage_label="FAILOVER", writer=writer)
])

device_ip = "127.0.0.1"
device_port = 5020
device_id = 1

factory = Pac3220ModbusFactory([ModbusTcpRegister.from_dict(d) for d in config["registers"]])

reader = Pac3220ModbusReader(device_ip, device_port, device_id, factory, storage_engine)

try:
    logger.info("Attempting to read data from device...")
    reader.read_and_store()
    logger.info("Data read successfully.")
except Exception as e:
    logger.error(f"An error occurred: {e}")