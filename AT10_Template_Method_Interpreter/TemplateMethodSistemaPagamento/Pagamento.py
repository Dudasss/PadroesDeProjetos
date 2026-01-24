from abc import ABC, abstractmethod


class Pagamento(ABC):
    def realizar_pagamento(self) -> None:
        self._imprimir_cabecalho()
        self._validar()
        self._processar()
        self._enviar_confirmacao()
        print('-' * 30)

    def _enviar_confirmacao(self) -> None:
        print("Confirmação de pagamento enviada.")

    @abstractmethod
    def _imprimir_cabecalho(self) -> None:
        pass

    @abstractmethod
    def _validar(self) -> None:
        pass

    @abstractmethod
    def _processar(self) -> None:
        pass
