from SistemaDeNotificaçõesMultiplataformas.Interface.INotificacao import INotificacao


class NotificacaoPushMobile(INotificacao):
    def enviar(self) -> str:
        return f"Enviando notificação por Push no seu dispositivo mobile."
