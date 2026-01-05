from AT9_Visitor_Memento_Mediator.SistemaChat.Classes.ChatMediator import ChatMediator
from AT9_Visitor_Memento_Mediator.SistemaChat.Classes.UsuarioChat import UsuarioChat


def SistemaChat():
    # criando o mediador
    chat_mediator = ChatMediator()

    # criando usuários
    alice = UsuarioChat(chat_mediator, "Alice")
    bob = UsuarioChat(chat_mediator, "Bob")
    carol = UsuarioChat(chat_mediator, "Carol")

    # registrando users no chat
    chat_mediator.adicionar_usuario(alice)
    chat_mediator.adicionar_usuario(bob)
    chat_mediator.adicionar_usuario(carol)

    # trocas de mensagens
    print("--- Início do Chat ---")
    alice.enviar("Olá, pessoal!")
    print("-" * 20)
    bob.enviar("Oi, Alice!")
    print("-" * 20)
    carol.enviar("Bom dia a todos Spam!")


if __name__ == "__main__":
    SistemaChat()
