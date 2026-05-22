from abc import ABC, abstractmethod
from typing import Generic

from Protocol import T


class IStorage(ABC, Generic[T]):
    """The core abstraction for any data persistence layer."""
    @abstractmethod
    def write(self, data: T) -> None:
        """Returns True if write succeeded, False if it failed."""
        pass