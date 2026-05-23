from typing import Dict, Any, TypeVar, Protocol

class Serializable(Protocol):
    """Any dataclass or object passed into our generic storage must
    implement this structural protocol so the CSV writer knows how to handle it."""
    def to_dict(self) -> Dict[str, Any]:
        pass

T = TypeVar('T', bound=Serializable)


class DictWrapper(Serializable):
    def __init__(self, data: Dict[str, Any]):
        self.data = data

    def to_dict(self) -> Dict[str, Any]:
        return self.data
