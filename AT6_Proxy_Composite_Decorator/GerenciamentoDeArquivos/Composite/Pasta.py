from typing import List

from AT6_Proxy_Composite_Decorator.GerenciamentoDeArquivos.Interface.ComponenteArquivoInterface import \
    ComponenteArquivoInterface


class Pasta(ComponenteArquivoInterface):
    def __init__(self, nome: str):
        self.nome = nome
        self._filhos: List[ComponenteArquivoInterface] = []

    def adicionar(self, componente: ComponenteArquivoInterface) -> None:
        self._filhos.append(componente)

    def remover(self, componente: ComponenteArquivoInterface) -> None:
        self._filhos.remove(componente)

    def exibir(self, identacao: str = "") -> None:
        print(f"{identacao}+ Pasta: {self.nome}")
        for filhos in self._filhos:
            filhos.exibir(identacao + " ")
