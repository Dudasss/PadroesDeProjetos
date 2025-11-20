from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.AdapterProcessamentoPagamentos.Classes.MercadoPagoAPI import \
    MercadoPagoAPI
from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.AdapterProcessamentoPagamentos.Interface.PagamentoInterface import \
    PagamentoInterface


class MercadoPagoAdapter(PagamentoInterface):
    def __init__(self, mercado_pago_service: MercadoPagoAPI):
        # recebendo o serviço MercadoPagoPI
        self.mercado_pago_service = mercado_pago_service

    def processar_pagamento(self, valor: float) -> None:
        # adaptando a classe MercadoPagoPI ao metodo esperado da interface PagamentoInterface
        self.mercado_pago_service.transacao_pagamento(valor)
