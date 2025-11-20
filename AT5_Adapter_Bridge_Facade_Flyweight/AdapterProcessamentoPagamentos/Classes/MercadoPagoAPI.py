class MercadoPagoAPI:
    def transacao_pagamento(self, valor_pagamento: float) -> None:
        # simulando processamento de pagamento do Mercado Pago
        print(f"[Mercado Pago]: Enviando pagamento de R${valor_pagamento:.2f}")
