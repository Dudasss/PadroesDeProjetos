from SistemaDeNotificações.Classes.NotificacaoSMS import NotificacaoSMS
from SistemaDeNotificações.Factory.NotificacaoFactory import NotificacaoFactory
from SistemaDeNotificações.Interface.INotificacao import INotificacao


class SMSNotificacaoFactory(NotificacaoFactory):
    # actory que cria notificações por E-mail
    def criar_notificacao(self) -> INotificacao:
        return NotificacaoSMS()
