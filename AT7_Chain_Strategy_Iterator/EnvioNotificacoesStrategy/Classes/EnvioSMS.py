from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.EnvioNotificacoesStrategy.Interface.EstrategiaEnvioInterface import \
    EstrategiaEnvioInterface


class EnvioSMS(EstrategiaEnvioInterface):
    def enviar(self, destinatario: str, mensagem: str) -> None:
        print(f"Enviando SMS para {destinatario}, {mensagem}")
