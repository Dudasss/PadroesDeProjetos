from AT9_Visitor_Memento_Mediator.ProcessamentoDocumentos.Classes import TXT, DOCX, PDF
from AT9_Visitor_Memento_Mediator.ProcessamentoDocumentos.Interfaces.Visitante import Visitante


class ExportacaoVisitor(Visitante):
    def visitar_pdf(self, pdf: PDF) -> None:
        print("Exportando PDF para XML...")

    def visitar_docx(self, docx: DOCX) -> None:
        print("Exportando DOCX para JSON...")

    def visitar_txt(self, txt: TXT) -> None:
        print("Exportando TXT para JSON...")
