from SistemaDeNotificações.Factory.EmailNotificacaoFactory import EmailNotificacaoFactory
from SistemaDeNotificações.Factory.NotificacaoFactory import NotificacaoFactory
from SistemaDeNotificações.Factory.PushNotificacaoFactory import PushNotificacaoFactory
from SistemaDeNotificações.Factory.SMSNotificacaoFactory import SMSNotificacaoFactory
from SistemaDeNotificações.Factory.WhatsAppNotificacaoFactory import WhatsAppNotificacaoFactory


def cliente_code(factory: NotificacaoFactory):
    print(f"Cliente: Usando a factory: {factory.__class__.__name__}")
    resultado_envio = factory.logica_de_envio()
    print(resultado_envio)


if __name__ == "__main__":
    print("Iniciando utilização do sistema de notificações...")
    # Enviar um E-mail
    print("\n--- E-mail ---")
    cliente_code(EmailNotificacaoFactory())

    # Enviar um SMS
    print("\n--- SMS ---")
    cliente_code(SMSNotificacaoFactory())

    # Enviar um Push
    print("\n--- Push ---")
    cliente_code(PushNotificacaoFactory())

    # Enviar um WhatsApp
    # demonstrando o prinicio Open Closed ao adicionar mais um tipo de notificação sem alterar o codigo
    print("\n--- WhatsApp ---")
    cliente_code(WhatsAppNotificacaoFactory())
