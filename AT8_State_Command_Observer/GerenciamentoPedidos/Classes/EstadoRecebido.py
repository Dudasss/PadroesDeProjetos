from typing import TYPE_CHECKING
from ..Interface.EstadoPedido import EstadoPedido

if TYPE_CHECKING:
    from .Pedido import Pedido


class EstadoRecebido(EstadoPedido):
    # após pedido recebido, o estado transita para o processamento
    def processar(self, pedido: 'Pedido') -> None:
        print("Pedido recebido. Iniciando processamento...")
        from .EstadoProcessando import EstadoProcessando
        pedido.definir_estado(EstadoProcessando())
