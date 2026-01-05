from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def enviar_mensagem(self, mensagem: str, usuario: 'Usuario') -> None:
        pass
