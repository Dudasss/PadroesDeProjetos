from abc import ABC, abstractmethod


class Observador(ABC):
    @abstractmethod
    def atualizar(self, nome_projeto: str, mensagem: str) -> None:
        pass
    