class SistemaPagamento:
    def processar_pagamento(self, valor: float) -> bool:
        print(f"Processando pagamento de R${valor:.2f}...")
        print("Pagamento aprovado.")
        return True
