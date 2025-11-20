from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.BridgeAutomacaoResidencial.ClassesControle.Controle import Controle


class PainelControle(Controle):
    def ativar(self) -> None:
        print("Utilizando o Painel de Controle.")
        super().ativar()

    def desativar(self) -> None:
        print("Utilizando o Painel de Controle.")
        super().desativar()
