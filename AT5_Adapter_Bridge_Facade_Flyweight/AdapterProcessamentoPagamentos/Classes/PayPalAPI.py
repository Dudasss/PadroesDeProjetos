class PayPalAPI:
    def send_payment(self, amount: float) -> None:
        # simulando processamento de pagamento do PayPal
        print(f"[PayPal]: Enviando pagamento de R${amount:.2f}")
