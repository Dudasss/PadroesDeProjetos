from abc import ABC, abstractmethod

from AT9_Visitor_Memento_Mediator.ProcessamentoDocumentos.Interfaces import Visitante


class Documento(ABC):
    @abstractmethod
    def aceitar(self, visitante: Visitante) -> None:
        pass
