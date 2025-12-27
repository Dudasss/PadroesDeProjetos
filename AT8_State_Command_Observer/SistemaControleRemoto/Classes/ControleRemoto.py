from typing import List

from PadroesDeProjetos.AT8_State_Command_Observer.SistemaControleRemoto.Interface import Comando


class ControleRemoto:
    def __init__(self):
        self._historico_comandos: List[Comando] = []

    def executar_comando(self, comando: Comando) -> None:
        comando.executar()
        self._historico_comandos.append(comando)

    def desfazer_ultimo_comando(self) -> None:
        if self._historico_comandos:
            ultimo_comando = self._historico_comandos.pop()
            ultimo_comando.desfazer()
        else:
            print("Nenhum comando para desfazer.")
