from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.AdapterProcessamentoPagamentos.Classes import PayPalAPI
from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.AdapterProcessamentoPagamentos.Interface.PagamentoInterface import \
    PagamentoInterface


class PayPalAdapter(PagamentoInterface):
    def __init__(self, paypal_service: PayPalAPI):
        # recebendo o serviço PayPalAPI
        self.paypal_service = paypal_service

    def processar_pagamento(self, valor: float) -> None:
        # adaptando a classe PayPalAPI ao metodo esperado da interface PagamentoInterface
        self.paypal_service.send_payment(valor)
