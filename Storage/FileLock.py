import fcntl
from pathlib import Path


class FileLock:
    def __init__(self, file_lock_path: Path):
        self.file_lock_path = file_lock_path
        self.file = open(self.file_lock_path, "a")

    def __enter__(self):
        fcntl.flock(self.file.fileno(), fcntl.LOCK_EX)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            fcntl.flock(self.file.fileno(), fcntl.LOCK_UN)

    def __del__(self):
        try:
            self.file.close()
        except Exception:
            pass
