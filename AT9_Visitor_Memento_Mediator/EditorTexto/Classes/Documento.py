from AT9_Visitor_Memento_Mediator.EditorTexto.Classes.Memento import Memento


class Documento:
    def __init__(self) -> None:
        self._conteudo: str = ""

    def escrever(self, texto: str) -> None:
        self._conteudo = texto

    def salvar_estado(self) -> Memento:
        return Memento(self._conteudo)

    def restaurar(self, memento: Memento) -> None:
        self._conteudo = memento.get_conteudo()

    def __str__(self) -> str:
        return f"Conteúdo do Documento: {self._conteudo}"
