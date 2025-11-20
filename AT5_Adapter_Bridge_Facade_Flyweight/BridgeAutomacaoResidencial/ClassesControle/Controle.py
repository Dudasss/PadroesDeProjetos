from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.BridgeAutomacaoResidencial.Interface.DispositivoInterface import \
    DispositivoInterface


class Controle:
    def __init__(self, dispositivo: DispositivoInterface):
        self.dispositivo = dispositivo

    def ativar(self) -> None:
        self.dispositivo.ligar()

    def desativar(self) -> None:
        self.dispositivo.desligar()
