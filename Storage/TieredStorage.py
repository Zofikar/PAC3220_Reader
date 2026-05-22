import logging
from typing import List

from Protocol import T
from Storage import IStorage
from datetime import datetime

logger = logging.getLogger("TieredStorage")

class TieredStorage(IStorage[T]):
    """Chains generic storage implementations together."""
    def __init__(self, storage_pipeline: List[IStorage[T]]):
        self.storage_pipeline = storage_pipeline

    def write(self, data: T):
        for storage_engine in self.storage_pipeline:
            try:
                storage_engine.write(data)
                return
            except Exception as e:
                logger.warning(e)
        raise Exception("No storage engine available.")