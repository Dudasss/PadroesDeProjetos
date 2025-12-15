from abc import ABC, abstractmethod


class ComponenteArquivoInterface(ABC):
    @abstractmethod
    def exibir(self, identacao: str = "") -> None:
        pass
