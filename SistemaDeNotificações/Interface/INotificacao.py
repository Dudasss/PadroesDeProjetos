from abc import ABC, abstractmethod


class INotificacao(ABC):
    @abstractmethod
    def enviar(self) -> str:
        # método abstrato que será implementado por cada notificação
        pass
