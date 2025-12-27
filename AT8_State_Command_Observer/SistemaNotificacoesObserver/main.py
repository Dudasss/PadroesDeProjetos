from PadroesDeProjetos.AT8_State_Command_Observer.SistemaNotificacoesObserver.Classes.Projeto import Projeto
from PadroesDeProjetos.AT8_State_Command_Observer.SistemaNotificacoesObserver.Classes.Usuario import Usuario


def SistemaNotificacao():
    # Criação do Projeto (Sujeito)
    projeto_dev = Projeto("Desenvolvimento de Software")

    # Criação dos Usuários (Observadores)
    alice = Usuario("Alice")
    bob = Usuario("Bob")

    # Inscrição dos usuários
    projeto_dev.anexar(alice)
    projeto_dev.anexar(bob)

    # Primeira alteração (Ambos recebem)
    projeto_dev.realizar_alteracao("Adicionadas novas funcionalidades ao sistema.")

    # Alice sai do projeto (Desanexar)
    projeto_dev.desanexar(alice)

    # Segunda alteração (Apenas Bob recebe)
    projeto_dev.realizar_alteracao("Correção de bugs realizados.")


if __name__ == "__main__":
    SistemaNotificacao()
