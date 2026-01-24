from PadroesDeProjetos.AT10_Template_Method_Interpreter.TemplateMethodSistemaPagamento.PagamentoCartaoCredito import \
    PagamentoCartaoCredito
from PadroesDeProjetos.AT10_Template_Method_Interpreter.TemplateMethodSistemaPagamento.PagamentoPayPal import PagamentoPayPal


def SistemaConsultas():
    # Instanciando as subclasses
    pagamento_cartao = PagamentoCartaoCredito()
    pagamento_paypal = PagamentoPayPal()

    # O cliente apenas chama o método público principal
    pagamento_cartao.realizar_pagamento()
    pagamento_paypal.realizar_pagamento()


if __name__ == "__main__":
    SistemaConsultas()
