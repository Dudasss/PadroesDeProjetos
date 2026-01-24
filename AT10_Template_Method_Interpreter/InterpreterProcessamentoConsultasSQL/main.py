from PadroesDeProjetos.AT10_Template_Method_Interpreter.InterpreterProcessamentoConsultasSQL.ConsultaSelect import ConsultaSelect
from PadroesDeProjetos.AT10_Template_Method_Interpreter.InterpreterProcessamentoConsultasSQL.ConsultaWhere import ConsultaWhere
from PadroesDeProjetos.AT10_Template_Method_Interpreter.InterpreterProcessamentoConsultasSQL.Contexto import Contexto
from typing import List, Dict, Any

class SistemaConsultas:
    def executar(self):
        dados_mock = [
            {"produto": "camiseta", "preco": 29.99},
            {"produto": "calça", "preco": 49.99},
            {"produto": "meia", "preco": 10.00}
        ]
        contexto = Contexto(dados_mock)

        print("Resultados da consulta SELECT:")
        select = ConsultaSelect(["produto", "preco"])
        resultado_select = select.interpretar(contexto)
        self.exibir_resultados(resultado_select)

        print("-" * 30)  # Separador visual

        print("Resultados da consulta WHERE:")
        where = ConsultaWhere("produto", "calça")
        resultado_where = where.interpretar(contexto)
        self.exibir_resultados(resultado_where)

    def exibir_resultados(self, lista_resultados: List[Dict[str, Any]]):
        if not lista_resultados:
            print("Nenhum resultado encontrado.")
            return

        for linha in lista_resultados:
            itens_formatados = [f"{k}:{v}" for k, v in linha.items()]

            print(";".join(itens_formatados))


# --- Execução do Sistema ---
if __name__ == "__main__":
    sistema = SistemaConsultas()
    sistema.executar()