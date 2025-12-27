from typing import TYPE_CHECKING
from ..Interface.EstadoPedido import EstadoPedido
if TYPE_CHECKING:
    from .Pedido import Pedido


class EstadoProcessando(EstadoPedido):
    # após pedido processado, o estado transita para o envio
    def processar(self, pedido: 'Pedido') -> None:
        print("Pedido está em processamento. Preparando para envio...")
        from .EstadoEnviado import EstadoEnviado
        pedido.definir_estado(EstadoEnviado())
