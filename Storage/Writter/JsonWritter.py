import json
import logging
import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any

from .IWriter import IWriter

logger = logging.getLogger(__name__)

class JsonWriter(IWriter):

    def write(self, new_entry: dict[str, Any], file: Path):
        data: list[dict[str, Any]] = []
        if file.exists():
            with open(file, "r", encoding="utf-8") as _fp:
                try:
                    data = json.load(_fp)
                except Exception as e:
                    logger.warning(e)
                    (file.parent / "corrupted").mkdir(parents=True, exist_ok=True)
                    shutil.copy2(file,
                                 file.parent / "corrupted" / (datetime.now().strftime("%d.%m.%Y %H:%M") + ".json"))
        else:
            logger.info(f"File {file} doesn't exist")
        data.append(new_entry)
        with open(file, "w", encoding="utf-8") as _fp:
            json.dump(data, _fp, ensure_ascii=False, indent=4)
            _fp.flush()
            os.fsync(_fp.fileno())
