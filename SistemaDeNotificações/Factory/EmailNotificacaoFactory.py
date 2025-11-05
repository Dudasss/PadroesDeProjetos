from SistemaDeNotificações.Classes.NotificacaoEmail import NotificacaoEmail
from SistemaDeNotificações.Factory.NotificacaoFactory import NotificacaoFactory
from SistemaDeNotificações.Interface.INotificacao import INotificacao


class EmailNotificacaoFactory(NotificacaoFactory):
    # actory que cria notificações por E-mail
    def criar_notificacao(self) -> INotificacao:
        return NotificacaoEmail()
