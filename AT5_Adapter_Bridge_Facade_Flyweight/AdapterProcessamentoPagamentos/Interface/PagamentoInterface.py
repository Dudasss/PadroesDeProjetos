from abc import ABC, abstractmethod


class PagamentoInterface(ABC):
    """
    Interface que define o contrato padrão para processar pagamentos no sistema.
    """
    @abstractmethod
    def processar_pagamento(self, valor: float) -> None:
        """
        Método abstrato que deve ser implementado por qualquer
        processador de pagamento compatível com o sistema.
        """
        pass
