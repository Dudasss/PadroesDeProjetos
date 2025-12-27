from typing import TYPE_CHECKING
from ..Interface.EstadoPedido import EstadoPedido
if TYPE_CHECKING:
    from .Pedido import Pedido


class EstadoEnviado(EstadoPedido):
    # após pedido enviado, o estado transita para entrega
    def processar(self, pedido: 'Pedido') -> None:
        print("Pedido enviado. Saindo para entrega...")
        from .EstadoEntregue import EstadoEntregue
        pedido.definir_estado(EstadoEntregue())
