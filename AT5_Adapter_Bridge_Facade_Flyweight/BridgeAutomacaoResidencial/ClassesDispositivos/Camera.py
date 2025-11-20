from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.BridgeAutomacaoResidencial.Interface.DispositivoInterface import \
    DispositivoInterface


class Camera(DispositivoInterface):
    def ligar(self):
        print("Câmera ligado")
    def desligar(self):
        print("Câmera desligado")
