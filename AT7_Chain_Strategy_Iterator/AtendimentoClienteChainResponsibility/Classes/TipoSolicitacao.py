from enum import Enum, auto


class TipoSolicitacao(Enum):
    CONSULTA = auto()
    RECLAMACAO = auto()
    SUGESTAO = auto()
    OUTRO = auto()
