from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.AdapterProcessamentoPagamentos.Adapters.MercadoPagoAdapter import \
    MercadoPagoAdapter
from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.AdapterProcessamentoPagamentos.Adapters.PayPalAdapter import \
    PayPalAdapter
from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.AdapterProcessamentoPagamentos.Adapters.StripeAdapter import \
    StripeAdapter
from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.AdapterProcessamentoPagamentos.Classes.MercadoPagoAPI import \
    MercadoPagoAPI
from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.AdapterProcessamentoPagamentos.Classes.PagamentoInterno import \
    PagamentoInterno
from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.AdapterProcessamentoPagamentos.Classes.PayPalAPI import \
    PayPalAPI
from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.AdapterProcessamentoPagamentos.Classes.StripeAPI import \
    StripeAPI


def pagar_interno(valor: float):
    processador = PagamentoInterno()
    processador.processar_pagamento(valor)


def pagar_paypal(valor: float):
    servico_paypal = PayPalAPI()
    processador = PayPalAdapter(servico_paypal)
    processador.processar_pagamento(valor)


def pagar_stripe(valor: float):
    servico_stripe = StripeAPI()
    processador = StripeAdapter(servico_stripe)
    processador.processar_pagamento(valor)


def pagar_mercado_pago(valor: float):
    servico_mercado_pago = MercadoPagoAPI()
    processador = MercadoPagoAdapter(servico_mercado_pago)
    processador.processar_pagamento(valor)


def main():
    valor_compra = 150
    metodo_pagamento = int(
        input("Digite\n1: Pagamento Interno\n2: Pagamento PayPal\n3: Pagamento Stripe\n4: Mercado Pago\n"))

    if metodo_pagamento == 1:
        pagar_interno(valor_compra)
    elif metodo_pagamento == 2:
        pagar_paypal(valor_compra)
    elif metodo_pagamento == 3:
        pagar_stripe(valor_compra)
    elif metodo_pagamento == 4:
        pagar_mercado_pago(valor_compra)
    else:
        print(f"Erro ao processar.")


if __name__ == "__main__":
    main()
