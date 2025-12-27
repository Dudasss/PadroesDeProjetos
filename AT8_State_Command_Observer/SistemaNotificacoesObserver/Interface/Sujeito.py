from abc import ABC, abstractmethod

from PadroesDeProjetos.AT8_State_Command_Observer.SistemaNotificacoesObserver.Interface import Observador


class Sujeito(ABC):
    @abstractmethod
    def anexar(self, observador: Observador) -> None:
        pass

    @abstractmethod
    def desanexar(self, observador: Observador) -> None:
        pass

    @abstractmethod
    def notificar(self, mensagem: str) -> None:
        pass
