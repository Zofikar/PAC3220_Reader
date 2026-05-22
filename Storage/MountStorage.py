import logging
import subprocess
from collections.abc import Callable
from datetime import datetime
from pathlib import Path

from Protocol import T
from Storage import IStorage, FsStorage

logger = logging.getLogger("MountStorage")

class MountStorage(IStorage[T]):
    """Hot-mount wrapper that passes the invariant type down to its internal writer."""

    def __init__(self, deviceFactory: Callable[[], Path], mount_point: Path, filename: str, storage_label: str):
        self.deviceFactory = deviceFactory
        self.mount_point = mount_point
        target_file_path = mount_point / filename

        self.delegate_storage = FsStorage[T](target_file_path=target_file_path, storage_label=storage_label)

    def _is_mounted(self) -> bool:
        return self.mount_point.is_mount()

    def _try_mount(self, device: Path) -> bool:
        if not device.exists():
            return False
        if self._is_mounted():
            return True
        try:
            self.mount_point.mkdir(parents=True, exist_ok=True)
            subprocess.run(
                ["sudo", "mount", "-o", "umask=000", str(device), str(self.mount_point)],
                check=True, capture_output=True
            )
            return True
        except subprocess.CalledProcessError as e:
            logger.error(e)
            return False

    def _safely_unmount(self):
        if self._is_mounted():
            try:
                subprocess.run(["sync"])
                subprocess.run(["sudo", "umount", str(self.mount_point)], check=True)
            except subprocess.CalledProcessError as e:
                logger.error(e)

    def write(self, data: T):
        try:
            device = self.deviceFactory()
            if not self._try_mount(device):
                print(f"[{datetime.now()}] MountStorage Error: Device {self.device} missing.")
                return False
            self.delegate_storage.write(data)
        finally:
            self._safely_unmount()