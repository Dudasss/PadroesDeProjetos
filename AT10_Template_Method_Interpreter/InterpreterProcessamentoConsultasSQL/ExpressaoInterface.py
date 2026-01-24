from abc import ABC, abstractmethod
from typing import List, Dict, Any

from PadroesDeProjetos.AT10_Template_Method_Interpreter.InterpreterProcessamentoConsultasSQL.Contexto import Contexto


class Expressao(ABC):
    @abstractmethod
    def interpretar(self, contexto: Contexto) -> List[Dict[str, Any]]:
        pass
