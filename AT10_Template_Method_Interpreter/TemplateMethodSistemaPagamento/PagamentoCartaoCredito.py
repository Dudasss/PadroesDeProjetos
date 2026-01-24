from PadroesDeProjetos.AT10_Template_Method_Interpreter.TemplateMethodSistemaPagamento.Pagamento import Pagamento


class PagamentoCartaoCredito(Pagamento):
    def _imprimir_cabecalho(self) -> None:
        print("Processando pagamento com cartão de crédito.")

    def _validar(self) -> None:
        print("Validando pagamento com cartão de crédito.")

    def _processar(self) -> None:
        print("Processando pagamento com cartão de crédito.")
