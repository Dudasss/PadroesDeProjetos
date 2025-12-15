from AT6_Proxy_Composite_Decorator.GerenciamentoDeArquivos.Interface.ComponenteArquivoInterface import \
    ComponenteArquivoInterface


class Arquivo(ComponenteArquivoInterface):
    def __init__(self, nome: str):
        self.nome = nome

    def exibir(self, identacao: str = "") -> None:
        print(f"{identacao}- Arquivo: {self.nome}")
