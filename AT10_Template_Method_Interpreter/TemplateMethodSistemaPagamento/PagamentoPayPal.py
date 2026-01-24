from PadroesDeProjetos.AT10_Template_Method_Interpreter.TemplateMethodSistemaPagamento.Pagamento import Pagamento


class PagamentoPayPal(Pagamento):
    def _imprimir_cabecalho(self) -> None:
        print("Processando pagamento via PayPal.")

    def _validar(self) -> None:
        print("Validando pagamento via PayPal.")

    def _processar(self) -> None:
        print("Processando pagamento via PayPal.")
