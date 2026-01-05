from abc import ABC, abstractmethod

from AT9_Visitor_Memento_Mediator.ProcessamentoDocumentos.Classes import PDF, DOCX, TXT


class Visitante(ABC):
    @abstractmethod
    def visitar_pdf(self, pdf: PDF) -> None:
        pass

    @abstractmethod
    def visitar_docx(self, docx: DOCX) -> None:
        pass

    @abstractmethod
    def visitar_txt(self, txt: TXT) -> None:
        pass
