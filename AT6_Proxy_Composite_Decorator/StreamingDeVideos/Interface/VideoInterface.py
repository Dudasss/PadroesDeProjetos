from abc import ABC, abstractmethod


class VideoInterface(ABC):
    @abstractmethod
    def exibir(self) -> None:
        pass
    