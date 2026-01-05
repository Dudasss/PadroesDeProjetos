from abc import ABC, abstractmethod

from AT9_Visitor_Memento_Mediator.SistemaChat.Interfaces.Mediator import Mediator


class Usuario(ABC):
    def __init__(self, mediator: Mediator, nome: str) -> None:
        self.mediator = mediator
        self.nome = nome

    @abstractmethod
    def enviar(self, mensagem: str) -> None:
        pass

    @abstractmethod
    def receber(self, mensagem: str) -> None:
        pass
