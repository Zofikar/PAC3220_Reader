from abc import ABC, abstractmethod
from typing import Generic

from Protocol import T
from Storage import IStorage


class IReader(ABC, Generic[T]):
    def __init__(self, storage_engine: IStorage[T]):
        self.storage_engine = storage_engine

    @abstractmethod
    def read(self) -> T:
        pass

    def read_and_store(self) -> None:
        self.storage_engine.write(self.read())