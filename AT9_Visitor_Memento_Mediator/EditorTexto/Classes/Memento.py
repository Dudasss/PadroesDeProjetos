class Memento:
    def __init__(self, conteudo: str) -> None:
        self._conteudo = conteudo

    def get_conteudo(self) -> str:
        return self._conteudo
