from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.EnvioNotificacoesStrategy.Interface.EstrategiaEnvioInterface import \
    EstrategiaEnvioInterface


class Notificador:
    def __init__(self, estrategia: EstrategiaEnvioInterface):
        self._estrategia = estrategia

    @property
    def estrategia(self) -> EstrategiaEnvioInterface:
        return self._estrategia

    @estrategia.setter
    def estrategia(self, nova_estrategia: EstrategiaEnvioInterface) -> None:
        print(f"Trocando de estrategia.")
        self._estrategia = nova_estrategia

    def notificar(self, destinatario: str, mensagem: str) -> None:
        self._estrategia.enviar(destinatario,mensagem)
