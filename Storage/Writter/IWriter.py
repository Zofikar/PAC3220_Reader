from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class IWriter(ABC):

    @abstractmethod
    def write(self, data: dict[str, Any], file: Path) -> None:
        """
        Writes a single record to the CSV file.

        Must ensure that the fieldnames used cover the union of keys found across all calls.
        If a key is present in the header but missing in 'data', its value in the row must be None.
        If a key is present in 'data' but not in the header, the header must be updated
        for subsequent writes, and this key's value must be used.

        Note: This abstract method relies on the concrete implementation maintaining
        or accessing the full set of required fieldnames across multiple calls.
        """
        raise NotImplementedError("Subclasses must implement write() to handle dynamic and evolving field headers.")
