from abc import ABC, abstractmethod
import copy


class DocumentoPrototipo(ABC):
    @abstractmethod
    def clone(self):
        pass
