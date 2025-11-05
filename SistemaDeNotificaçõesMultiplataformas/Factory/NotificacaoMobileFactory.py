from SistemaDeNotificaçõesMultiplataformas.Classes.NotificacaoEmailMobile import NotificacaoEmailMobile
from SistemaDeNotificaçõesMultiplataformas.Classes.NotificacaoPushMobile import NotificacaoPushMobile
from SistemaDeNotificaçõesMultiplataformas.Classes.NotificacaoSMSMobile import NotificacaoSMSMobile
from SistemaDeNotificaçõesMultiplataformas.Interface.INotificacao import INotificacao
from SistemaDeNotificaçõesMultiplataformas.Interface.NotificacaoFactory import NotificacaoFactory


class NotificacaoMobileFactory(NotificacaoFactory):
    def criar_notificacao_email(self) -> INotificacao:
        return NotificacaoEmailMobile()

    def criar_notificacao_sms(self) -> INotificacao:
        return NotificacaoSMSMobile()

    def criar_notificacao_push(self) -> INotificacao:
        return NotificacaoPushMobile()
