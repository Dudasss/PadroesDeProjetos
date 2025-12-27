from PadroesDeProjetos.AT8_State_Command_Observer.SistemaControleRemoto.Classes import Ventilador
from PadroesDeProjetos.AT8_State_Command_Observer.SistemaControleRemoto.Interface.Comando import Comando


class DesligarVentilador(Comando):
    def __init__(self, ventilador: Ventilador):
        self._ventilador = ventilador

    def executar(self) -> None:
        self._ventilador.desligar()

    def desfazer(self) -> None:
        self._ventilador.ligar()
