from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.EnvioNotificacoesStrategy.Interface.EstrategiaEnvioInterface import \
    EstrategiaEnvioInterface


class EnvioWhatsApp(EstrategiaEnvioInterface):
    def enviar(self, destinatario: str, mensagem: str) -> None:
        print(f"Enviando mensagem WhatsApp para {destinatario}, {mensagem}")
