from AT9_Visitor_Memento_Mediator.ProcessamentoDocumentos.Classes import PDF, DOCX, TXT
from AT9_Visitor_Memento_Mediator.ProcessamentoDocumentos.Interfaces.Visitante import Visitante


class ImpressaoVisitor(Visitante):
    def visitar_pdf(self, pdf: PDF) -> None:
        print(f"Imprimindo: Contedúdo do documento PDF -> {pdf.conteudo}")

    def visitar_docx(self, docx: DOCX) -> None:
        print(f"Imprimindo: Contedúdo do documento DOCX -> {docx.conteudo}")

    def visitar_txt(self, txt: TXT) -> None:
        print(f"Imprimindo: Contedúdo do documento TXT -> {txt.conteudo}")
