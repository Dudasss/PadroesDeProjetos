from AT9_Visitor_Memento_Mediator.SistemaChat.Interfaces.Usuario import Usuario


class UsuarioChat(Usuario):
    def enviar(self, mensagem: str) -> None:
        print(f"{self.nome} enviou: {mensagem}")
        self.mediator.enviar_mensagem(mensagem, self)

    def receber(self, mensagem: str) -> None:
        print(f"{self.nome} recebeu: {mensagem}")
