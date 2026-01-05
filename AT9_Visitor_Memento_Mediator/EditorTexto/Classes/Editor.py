from typing import List

from AT9_Visitor_Memento_Mediator.EditorTexto.Classes import Documento, Memento


class Editor:
    def __init__(self, documento: Documento) -> None:
        self._documento = documento
        self._historico: List[Memento] = []

    def escrever_e_salvar(self, texto: str) -> None:
        if self._documento._conteudo:
            self._historico.append(self._documento.salvar_estado())

        self._documento.escrever(texto)
        print(self._documento)

    def desfazer(self) -> None:
        if not self._historico:
            print("Nenhum estado para desfazer.")
            return

        memento = self._historico.pop()
        self._documento.restaurar(memento)
        print(self._documento)
