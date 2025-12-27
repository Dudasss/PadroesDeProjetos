from typing import List

from PadroesDeProjetos.AT8_State_Command_Observer.SistemaNotificacoesObserver.Interface import Observador
from PadroesDeProjetos.AT8_State_Command_Observer.SistemaNotificacoesObserver.Interface.Sujeito import Sujeito


class Projeto(Sujeito):
    def __init__(self, nome: str):
        self.nome = nome
        self._observadores: List[Observador] = []

    def anexar(self, observador: Observador) -> None:
        if observador not in self._observadores:
            self._observadores.append(observador)

    def desanexar(self, observador: Observador) -> None:
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar(self, mensagem: str) -> None:
        print(f"\nAtualizando projeto: {mensagem}")
        for observador in self._observadores:
            observador.atualizar(self.nome, mensagem)

    def realizar_alteracao(self, mensagem: str) -> None:
        self.notificar(mensagem)
