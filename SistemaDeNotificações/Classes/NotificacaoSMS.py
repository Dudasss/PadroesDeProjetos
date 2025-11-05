from SistemaDeNotificações.Interface.INotificacao import INotificacao


class NotificacaoSMS(INotificacao):
    def enviar(self) -> str:
        return f"Enviando notificação por SMS."
