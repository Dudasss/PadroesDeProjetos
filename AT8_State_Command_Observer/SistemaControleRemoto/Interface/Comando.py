from abc import ABC, abstractmethod


class Comando(ABC):
    @abstractmethod
    def executar(self) -> None:
        pass

    @abstractmethod
    def desfazer(self) -> None:
        pass
