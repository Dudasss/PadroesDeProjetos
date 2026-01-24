from typing import List, Dict, Any

from PadroesDeProjetos.AT10_Template_Method_Interpreter.InterpreterProcessamentoConsultasSQL.Contexto import Contexto
from PadroesDeProjetos.AT10_Template_Method_Interpreter.InterpreterProcessamentoConsultasSQL.ExpressaoInterface import Expressao


class ConsultaWhere(Expressao):
    def __init__(self, coluna: str, valor: Any):
        self.coluna = coluna
        self.valor = valor

    def interpretar(self, contexto: Contexto) -> List[Dict[str, Any]]:
        return [linha for linha in contexto.dados if linha.get(self.coluna) == self.valor]

