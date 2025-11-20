from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.BridgeAutomacaoResidencial.ClassesControle.Controle import Controle


class AplicativoMovel(Controle):
    def ativar(self) -> None:
        print("Utilizando o Aplicativo Móvel.")
        super().ativar()

    def desativar(self) -> None:
        print("Utilizando o Aplicativo Móvel.")
        super().desativar()
