import logging

from Protocol import T
from Storage import IStorage
from datetime import datetime
import csv
import os
from pathlib import Path

logger = logging.getLogger("FsStorage")

class FsStorage(IStorage[T]):
    """Directly writes data to a specified filesystem path."""

    def __init__(self, target_file_path: Path, storage_label: str):
        self.target_file_path = target_file_path
        self.storage_label = storage_label

    def write(self, data: T):
        payload = data.to_dict()

        file_exists = self.target_file_path.exists()
        self.target_file_path.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Writing data to {self.target_file_path}")
        with open(self.target_file_path, mode='a') as file:
            writer = csv.DictWriter(file, fieldnames=payload.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(payload)
            file.flush()
            os.fsync(file.fileno())
        logger.info(f"Data written to {self.target_file_path}")
