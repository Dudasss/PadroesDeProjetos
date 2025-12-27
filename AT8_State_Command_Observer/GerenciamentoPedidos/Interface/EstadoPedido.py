from abc import ABC, abstractmethod


class EstadoPedido(ABC):
    @abstractmethod
    def processar(self, pedido: 'Pedido') -> None:
        pass
