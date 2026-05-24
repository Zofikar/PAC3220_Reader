import logging
from pathlib import Path

from Protocol import T
from Storage.Writter import IWriter
from .IStorage import IStorage

logger = logging.getLogger("FsStorage")

class FsStorage(IStorage[T]):
    """Directly writes data to a specified filesystem path."""

    def __init__(self, target_file_path: Path, storage_label: str, writer: IWriter):
        self.target_file_path = target_file_path
        self.storage_label = storage_label
        self.writer = writer

    def write(self, data: T):
        payload = data.to_dict()

        self.target_file_path.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Writing data to {self.target_file_path}")
        self.writer.write(payload, self.target_file_path)
        logger.info(f"Data written to {self.target_file_path}")
