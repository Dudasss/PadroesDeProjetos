from typing import List

from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.BibliotecaIterator.Classes.BibliotecaIterator import \
    BibliotecaIterator
from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.BibliotecaIterator.Classes.Livro import Livro
from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.BibliotecaIterator.Interface.ColecaoInterface import ColecaoInterface
from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.BibliotecaIterator.Interface.IteratorInterface import \
    IteratorInterface


class Biblioteca(ColecaoInterface):
    def __init__(self):
        self._livros: List[Livro] = []

    def adicionar_livro(self, livro: Livro):
       self._livros.append(livro)

    def create_iterator(self) -> 'IteratorInterface':
        return BibliotecaIterator(self._livros)
