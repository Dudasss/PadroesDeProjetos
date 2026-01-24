from typing import List, Dict, Any

from PadroesDeProjetos.AT10_Template_Method_Interpreter.InterpreterProcessamentoConsultasSQL.Contexto import Contexto
from PadroesDeProjetos.AT10_Template_Method_Interpreter.InterpreterProcessamentoConsultasSQL.ExpressaoInterface import Expressao


class ConsultaSelect(Expressao):
    def __init__(self, colunas: List[str] = None):
        self.colunas = colunas

    def interpretar(self, contexto: Contexto) -> List[Dict[str, Any]]:
        if not self.colunas:
            return contexto.dados

        resultado = []
        for linha in contexto.dados:
            nova_linha = {k: v for k, v in linha.items() if k in self.colunas}
            resultado.append(nova_linha)

        return resultado