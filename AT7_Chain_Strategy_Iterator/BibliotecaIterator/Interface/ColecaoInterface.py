from abc import ABC, abstractmethod

from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.BibliotecaIterator.Interface.IteratorInterface import \
    IteratorInterface


class ColecaoInterface(ABC):
    @abstractmethod
    def create_iterator(self) -> 'IteratorInterface':
        pass
