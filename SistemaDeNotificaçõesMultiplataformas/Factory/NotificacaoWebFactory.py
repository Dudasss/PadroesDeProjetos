from SistemaDeNotificaçõesMultiplataformas.Classes.NotificacaoEmailWeb import NotificacaoEmailWeb
from SistemaDeNotificaçõesMultiplataformas.Classes.NotificacaoPushWeb import NotificacaoPushWeb
from SistemaDeNotificaçõesMultiplataformas.Classes.NotificacaoSMSWeb import NotificacaoSMSWeb
from SistemaDeNotificaçõesMultiplataformas.Interface.INotificacao import INotificacao
from SistemaDeNotificaçõesMultiplataformas.Interface.NotificacaoFactory import NotificacaoFactory


class NotificacaoWebFactory(NotificacaoFactory):
    def criar_notificacao_email(self) -> INotificacao:
        return NotificacaoEmailWeb()

    def criar_notificacao_sms(self) -> INotificacao:
        return NotificacaoSMSWeb()

    def criar_notificacao_push(self) -> INotificacao:
        return NotificacaoPushWeb()
