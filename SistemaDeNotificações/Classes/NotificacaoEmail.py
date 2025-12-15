from PadroesDeProjetos.SistemaDeNotificações.Interface.INotificacao import INotificacao


class NotificacaoEmail(INotificacao):
    def enviar(self) -> str:
        return f"Enviando notificação por E-mail."
