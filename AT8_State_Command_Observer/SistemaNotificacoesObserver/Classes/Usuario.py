from AT8_State_Command_Observer.SistemaNotificacoesObserver.Interface.Observador import Observador


class Usuario(Observador):
    def __init__(self, nome: str):
        self.nome = nome

    def atualizar(self, nome_projeto: str, mensagem: str) -> None:
        print(f"{self.nome}: O projeto '{nome_projeto}' foi atualizado: {mensagem}")
