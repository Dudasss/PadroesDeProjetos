from PadroesDeProjetos.AT8_State_Command_Observer.SistemaControleRemoto.Classes import Luz
from PadroesDeProjetos.AT8_State_Command_Observer.SistemaControleRemoto.Interface.Comando import Comando


class LigarLuz(Comando):
    def __init__(self, luz: Luz):
        self._luz = luz

    def executar(self) -> None:
        self._luz.ligar()

    def desfazer(self) -> None:
        self._luz.desligar()
