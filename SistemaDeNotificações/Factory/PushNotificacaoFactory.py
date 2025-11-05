from SistemaDeNotificações.Classes.NotificacaoPush import NotificacaoPush
from SistemaDeNotificações.Factory.NotificacaoFactory import NotificacaoFactory
from SistemaDeNotificações.Interface.INotificacao import INotificacao


class PushNotificacaoFactory(NotificacaoFactory):
    # actory que cria notificações por E-mail
    def criar_notificacao(self) -> INotificacao:
        return NotificacaoPush()
