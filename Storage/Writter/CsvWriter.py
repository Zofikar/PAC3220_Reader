import csv
import os
from pathlib import Path
from typing import Any

from .IWriter import IWriter


class CsvWriter(IWriter):

    @staticmethod
    def __read(file: Path) -> tuple[list[str], list[dict[str, Any]]]:
        if not file.exists():
            return [], []
        with open(file, "r", encoding='utf-8') as _fp:
            reader = csv.reader(_fp)
            try:
                header = next(reader)
            except StopIteration:
                return [], []
            data: list[dict[str, Any]] = [{key: value for key, value in zip(header, row)} for row in reader]
        return header, data

    def write(self, new_entry: dict[str, Any], file: Path):
        keys = set(new_entry.keys())
        header, data = self.__read(file)
        keys.update(header)
        data.append(new_entry)
        keys = sorted(list(keys))
        with open(file, "w", newline='', encoding='utf-8') as _fp:
            writer = csv.writer(_fp)
            writer.writerow(keys)
            writer.writerows([[entry.get(key) for key in keys] for entry in data])
            _fp.flush()
            os.fsync(_fp.fileno())
