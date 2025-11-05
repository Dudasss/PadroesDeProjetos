from abc import ABC, abstractmethod

from SistemaDeNotificaçõesMultiplataformas.Interface.INotificacao import INotificacao


class NotificacaoFactory(ABC):
    @abstractmethod
    def criar_notificacao_email(self) -> INotificacao:
        pass

    @abstractmethod
    def criar_notificacao_sms(self) -> INotificacao:
        pass

    @abstractmethod
    def criar_notificacao_push(self) -> INotificacao:
        pass
