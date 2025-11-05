from SistemaDeNotificações.Classes.NotificacaoWhatsApp import NotificacaoWhatsApp
from SistemaDeNotificações.Factory.NotificacaoFactory import NotificacaoFactory
from SistemaDeNotificações.Interface.INotificacao import INotificacao


class WhatsAppNotificacaoFactory(NotificacaoFactory):
    # actory que cria notificações por E-mail
    def criar_notificacao(self) -> INotificacao:
        return NotificacaoWhatsApp()
