from SistemaDeNotificaçõesMultiplataformas.Interface.INotificacao import INotificacao


class NotificacaoSMSWeb(INotificacao):
    def enviar(self) -> str:
        return f"Enviando notificação via SMS no seu dispositivo web."
