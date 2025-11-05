from abc import ABC, abstractmethod

from SistemaDeNotificações.Interface.INotificacao import INotificacao


class NotificacaoFactory(ABC):
    @abstractmethod
    def criar_notificacao(self) -> INotificacao:
        # método abstrato que será implementado por cada classe base
        pass

    def logica_de_envio(self) -> str:
        notificacao = self.criar_notificacao()
        resultado = notificacao.enviar()
        return f"{resultado}"
