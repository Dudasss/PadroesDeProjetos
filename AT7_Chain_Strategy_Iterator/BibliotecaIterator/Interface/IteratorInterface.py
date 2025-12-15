from abc import ABC, abstractmethod
from typing import Any


class IteratorInterface(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> Any:
        pass

    @abstractmethod
    def current_item(self) -> Any:
        pass
