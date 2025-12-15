from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.EnvioNotificacoesStrategy.Interface.EstrategiaEnvioInterface import \
    EstrategiaEnvioInterface


class EnvioEmail(EstrategiaEnvioInterface):
    def enviar(self, destinatario: str, mensagem: str) -> None:
        print(f"Enviando e-mail para {destinatario}, {mensagem}")
