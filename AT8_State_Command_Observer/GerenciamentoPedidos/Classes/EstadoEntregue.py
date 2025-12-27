from typing import TYPE_CHECKING
from ..Interface.EstadoPedido import EstadoPedido
if TYPE_CHECKING:
    from .Pedido import Pedido


class EstadoEntregue(EstadoPedido):
    # estado final
    def processar(self, pedido: 'Pedido') -> None:
        print("Pedido entregue ao destinatário!")
        pedido.definir_estado(EstadoEntregue())
