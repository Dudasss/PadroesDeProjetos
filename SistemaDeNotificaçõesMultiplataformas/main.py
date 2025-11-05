from SistemaDeNotificaçõesMultiplataformas.Factory.NotificacaoMobileFactory import NotificacaoMobileFactory
from SistemaDeNotificaçõesMultiplataformas.Factory.NotificacaoWebFactory import NotificacaoWebFactory
from SistemaDeNotificaçõesMultiplataformas.Interface.NotificacaoFactory import NotificacaoFactory


def enviar_todas_as_notificacoes(factory: NotificacaoFactory):
    """
    Função cliente que recebe uma fábrica abstrata.
    Ela não sabe qual fábrica concreta (Web ou Mobile) está usando,
    apenas usa os métodos de criação para obter os produtos
    e chamar seus métodos.
    """
    # Pede à fábrica para criar os produtos
    notif_email = factory.criar_notificacao_email()
    notif_sms = factory.criar_notificacao_sms()
    notif_push = factory.criar_notificacao_push()

    # Usa os produtos
    print(notif_email.enviar())
    print(notif_sms.enviar())
    print(notif_push.enviar())


# --- Simulação ---
if __name__ == "__main__":
    print("PLATAFORMA WEB")
    fabrica_web = NotificacaoWebFactory()
    enviar_todas_as_notificacoes(fabrica_web)

    print("\n" + "=" * 40 + "\n")
    print("PLATAFORMA MOBILE")
    fabrica_mobile = NotificacaoMobileFactory()
    enviar_todas_as_notificacoes(fabrica_mobile)
