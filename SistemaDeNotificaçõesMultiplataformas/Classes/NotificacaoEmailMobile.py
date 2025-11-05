from SistemaDeNotificaçõesMultiplataformas.Interface.INotificacao import INotificacao


class NotificacaoEmailMobile(INotificacao):
    def enviar(self) -> str:
        return f"Enviando notificação por E-mail no seu dispositivo mobile."
