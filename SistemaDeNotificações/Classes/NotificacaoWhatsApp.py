from SistemaDeNotificações.Interface.INotificacao import INotificacao


class NotificacaoWhatsApp(INotificacao):
    def enviar(self) -> str:
        return f"Enviando notificação por WhatsApp."
