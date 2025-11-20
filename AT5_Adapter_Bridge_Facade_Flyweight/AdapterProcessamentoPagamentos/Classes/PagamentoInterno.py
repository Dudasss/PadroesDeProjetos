from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.AdapterProcessamentoPagamentos.Interface.PagamentoInterface import \
    PagamentoInterface


class PagamentoInterno(PagamentoInterface):
    def processar_pagamento(self, valor: float) -> None:
        # simulando processamento de pagamento
        print(f"[Sistema Interno]: Processando pagamento de R${valor}")
