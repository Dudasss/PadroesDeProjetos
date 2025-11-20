from abc import ABC, abstractmethod


class DispositivoInterface(ABC):
    @abstractmethod
    def ligar(self) -> None:
        pass
    @abstractmethod
    def desligar(self) -> None:
        pass
    