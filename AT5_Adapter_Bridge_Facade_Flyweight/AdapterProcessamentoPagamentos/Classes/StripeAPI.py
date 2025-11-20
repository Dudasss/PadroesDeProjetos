class StripeAPI:
    def make_transaction(self, total: float, currency: str) -> None:
        # simulando processamento de pagamento do Stripe
        print(f"[Stripe]: Transação de {total:.2f} {currency} realizada.")
