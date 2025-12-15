from abc import ABC, abstractmethod


class EstrategiaEnvioInterface(ABC):
    @abstractmethod
    def enviar(self, destinatario: str, mensagem: str) -> None:
        pass
