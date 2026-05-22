from typing import List

from Protocol import T
from Storage import IStorage
from datetime import datetime

class TieredStorage(IStorage[T]):
    """Chains generic storage implementations together."""
    def __init__(self, storage_pipeline: List[IStorage[T]]):
        self.storage_pipeline = storage_pipeline

    def write(self, data: T):
        exceptions = []
        for storage_engine in self.storage_pipeline:
            try:
                storage_engine.write(data)
                return
            except Exception as e:
                exceptions.append(e)
        raise Exception("No storage engine available. [" + ' '.join(str(e) for e in exceptions) + ']')