from AT9_Visitor_Memento_Mediator.ProcessamentoDocumentos.Classes import PDF, DOCX, TXT
from AT9_Visitor_Memento_Mediator.ProcessamentoDocumentos.Interfaces.Visitante import Visitante


class VisualizacaoVisitor(Visitante):
    def visitar_pdf(self, pdf: PDF) -> None:
        print(f"Visualizando: Contedúdo do documento PDF -> {pdf.conteudo}")

    def visitar_docx(self, docx: DOCX) -> None:
        print(f"Visualizando: Contedúdo do documento DOCX -> {docx.conteudo}")

    def visitar_txt(self, txt: TXT) -> None:
        print(f"Visualizando: Contedúdo do documento TXT -> {txt.conteudo}")