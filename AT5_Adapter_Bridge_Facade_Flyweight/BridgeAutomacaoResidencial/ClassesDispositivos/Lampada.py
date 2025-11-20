from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.BridgeAutomacaoResidencial.Interface.DispositivoInterface import \
    DispositivoInterface


class Lampada(DispositivoInterface):
    def ligar(self):
        print("Lâmpada ligada")

    def desligar(self):
        print("Lâmpada desligada")
