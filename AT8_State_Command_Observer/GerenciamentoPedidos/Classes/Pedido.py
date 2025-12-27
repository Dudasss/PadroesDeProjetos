from __future__ import annotations

from PadroesDeProjetos.AT8_State_Command_Observer.GerenciamentoPedidos.Classes.EstadoRecebido import EstadoRecebido
from PadroesDeProjetos.AT8_State_Command_Observer.GerenciamentoPedidos.Interface import EstadoPedido


class Pedido:
    def __init__(self):
        self._estado: EstadoPedido = EstadoRecebido()

    def definir_estado(self, estado: EstadoPedido) -> None:
        self._estado = estado

    def processar_pedido(self) -> None:
        self._estado.processar(self)
