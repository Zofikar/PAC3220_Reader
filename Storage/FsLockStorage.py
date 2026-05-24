import logging
from pathlib import Path

from Protocol import T
from Storage import FsStorage, FileLock
from Storage.Writter import IWriter

logger = logging.getLogger("FsLockStorage")


class FsLockStorage(FsStorage[T]):
    """Directly writes data to a specified filesystem path, protected by a companion file lock."""

    def __init__(self, target_file_path: Path, storage_label: str, writer: IWriter):
        target_file_path.parent.mkdir(parents=True, exist_ok=True)
        super().__init__(target_file_path, storage_label, writer)
        self.lock = FileLock(target_file_path.with_name(target_file_path.name + ".lock"))

    def write(self, data: T):
        with self.lock:
            super().write(data)
