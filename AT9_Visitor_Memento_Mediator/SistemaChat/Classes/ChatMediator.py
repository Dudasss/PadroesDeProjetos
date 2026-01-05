from typing import List
from AT9_Visitor_Memento_Mediator.SistemaChat.Interfaces.Mediator import Mediator
from AT9_Visitor_Memento_Mediator.SistemaChat.Interfaces.Usuario import Usuario


class ChatMediator(Mediator):
    def __init__(self) -> None:
        self.usuarios: List[Usuario] = []

    def adicionar_usuario(self, usuario: Usuario) -> None:
        self.usuarios.append(usuario)

    def enviar_mensagem(self, mensagem: str, usuario_origem: Usuario) -> None:
        if "Spam" in mensagem:
            print("Mensagem bloqueada pelo mediador")
            return
        for usuario in self.usuarios:
            if usuario != usuario_origem:
                usuario.receber(mensagem)
