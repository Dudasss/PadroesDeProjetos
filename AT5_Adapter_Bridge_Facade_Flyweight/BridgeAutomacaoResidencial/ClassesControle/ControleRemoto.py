from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.BridgeAutomacaoResidencial.ClassesControle.Controle import Controle


class ControleRemoto(Controle):
    def ativar(self) -> None:
        print("Utilizando o Controle Remoto.")
        super().ativar()

    def desativar(self) -> None:
        print("Utilizando o Controle Remoto.")
        super().desativar()
