from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.BridgeAutomacaoResidencial.Interface.DispositivoInterface import \
    DispositivoInterface


class Ventilador(DispositivoInterface):
    def ligar(self):
        print("Ventilador ligado")

    def desligar(self):
        print("Ventilador desligado")
