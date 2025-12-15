from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.EnvioNotificacoesStrategy.Interface.EstrategiaEnvioInterface import \
    EstrategiaEnvioInterface


class EnvioPush(EstrategiaEnvioInterface):
    def enviar(self, destinatario: str, mensagem: str) -> None:
        print(f"Enviando notificação push para {destinatario}, {mensagem}")
