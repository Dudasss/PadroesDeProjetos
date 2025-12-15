from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.EnvioNotificacoesStrategy.Classes.EnvioEmail import EnvioEmail
from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.EnvioNotificacoesStrategy.Classes.EnvioPush import EnvioPush
from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.EnvioNotificacoesStrategy.Classes.EnvioSMS import EnvioSMS
from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.EnvioNotificacoesStrategy.Classes.EnvioWhatsApp import EnvioWhatsApp
from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.EnvioNotificacoesStrategy.Classes.Notificador import Notificador


def envio_notificacao():
    email = EnvioEmail()
    sms = EnvioSMS()
    push = EnvioPush()
    zap = EnvioWhatsApp()

    notificador = Notificador(email)
    notificador.notificar("teste@gmail.com", "Olá, este é um e-mail teste.")

    notificador.estrategia = sms
    notificador.notificar("+5574999999999", "Olá, este é um SMS teste.")

    notificador.estrategia = push
    notificador.notificar("teste123", "Olá, este é uma notificação teste.")

    notificador.estrategia = zap
    notificador.notificar("+5574999999999", "Olá, este é uma mensagem WhatsApp teste.")


if __name__ == "__main__":
    envio_notificacao()
