import json
import os
from pathlib import Path
from typing import Any

from .IWriter import IWriter


class JsonWriter(IWriter):

    def write(self, new_entry: dict[str, Any], file: Path):
        with open(file, "r", encoding="utf-8") as _fp:
            data: list[dict[str, Any]] = json.load(_fp)
        data.append(new_entry)
        with open(file, "w", encoding="utf-8") as _fp:
            json.dump(data, _fp, ensure_ascii=False, indent=4)
            _fp.flush()
            os.fsync(_fp.fileno())
