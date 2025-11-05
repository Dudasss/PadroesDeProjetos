from SistemaDeNotificaçõesMultiplataformas.Interface.INotificacao import INotificacao


class NotificacaoPushWeb(INotificacao):
    def enviar(self) -> str:
        return f"Enviando notificação por Push no seu dispositivo web."
