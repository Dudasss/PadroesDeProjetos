from SistemaDeNotificações.Interface.INotificacao import INotificacao


class NotificacaoPush(INotificacao):
    def enviar(self) -> str:
        return f"Enviando notificação via Push."
