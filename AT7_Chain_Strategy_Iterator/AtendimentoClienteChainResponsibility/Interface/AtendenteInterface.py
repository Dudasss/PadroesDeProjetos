from abc import ABC, abstractmethod
from typing import Optional

from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.AtendimentoClienteChainResponsibility.Classes import Solicitacao


class AtendenteInterface(ABC):
    def __init__(self):
        self._proximo_atendente: Optional[AtendenteInterface] = None

    def definir_proximo(self, atendente: 'AtendenteInterface') -> 'AtendenteInterface':
        self._proximo_atendente = atendente
        return atendente

    @abstractmethod
    def processar(self, solicitacao: Solicitacao) -> None:
        pass

    def passar_adiante(self, solicitacao: Solicitacao) -> None:
        if self._proximo_atendente:
            self._proximo_atendente.processar(solicitacao)
