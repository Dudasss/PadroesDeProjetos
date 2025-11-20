from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.AdapterProcessamentoPagamentos.Classes.StripeAPI import \
    StripeAPI
from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.AdapterProcessamentoPagamentos.Interface.PagamentoInterface import \
    PagamentoInterface


class StripeAdapter(PagamentoInterface):
    def __init__(self, stripe_service: StripeAPI):
        # recebendo o serviço PayPalAPI
        self.stripe_service = stripe_service

    def processar_pagamento(self, valor: float) -> None:
        # adaptando a classe StripeAPI ao metodo esperado da interface PagamentoInterface
        self.stripe_service.make_transaction(valor, "BRL")
