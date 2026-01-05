from AT9_Visitor_Memento_Mediator.ProcessamentoDocumentos.Interfaces import Visitante
from AT9_Visitor_Memento_Mediator.ProcessamentoDocumentos.Interfaces.Documento import Documento


class PDF(Documento):
    def __init__(self, conteudo: 'str'):
        self.conteudo = conteudo

    def aceitar(self, visitante: Visitante) -> None:
        visitante.visitar_pdf(self)
