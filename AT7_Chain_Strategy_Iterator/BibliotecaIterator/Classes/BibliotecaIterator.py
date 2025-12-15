from typing import List, Any

from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.BibliotecaIterator.Classes.Livro import Livro
from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.BibliotecaIterator.Interface.IteratorInterface import \
    IteratorInterface


class BibliotecaIterator(IteratorInterface):
    def __init__(self, livros: List[Livro]):
        self._livros = livros
        self._index = 0

    def has_next(self) -> bool:
        return self._index < len(self._livros)

    def next(self) -> Livro | None:
        if self.has_next():
            livro = self._livros[self._index]
            self._index += 1
            return livro
        return None

    def current_item(self) -> Livro | None:
        if self.has_next():
            return self._livros[self._index]
        return None
