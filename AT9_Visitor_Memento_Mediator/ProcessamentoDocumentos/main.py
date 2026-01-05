from typing import List

from AT9_Visitor_Memento_Mediator.ProcessamentoDocumentos.Classes.DOCX import DOCX
from AT9_Visitor_Memento_Mediator.ProcessamentoDocumentos.Classes.ExportacaoVisitor import ExportacaoVisitor
from AT9_Visitor_Memento_Mediator.ProcessamentoDocumentos.Classes.ImpressaoVisitor import ImpressaoVisitor
from AT9_Visitor_Memento_Mediator.ProcessamentoDocumentos.Classes.PDF import PDF
from AT9_Visitor_Memento_Mediator.ProcessamentoDocumentos.Classes.TXT import TXT
from AT9_Visitor_Memento_Mediator.ProcessamentoDocumentos.Classes.VisualizacaoVisitor import VisualizacaoVisitor
from AT9_Visitor_Memento_Mediator.ProcessamentoDocumentos.Interfaces import Documento


def processamento_docs():
    # criando uma lista de documentos
    documentos: List[Documento] = [
        PDF("Relatorio_Final.pdf"),
        DOCX("TCC_Versao_1.docx"),
        TXT("notas.txt")
    ]

    # instanciando os visitantes
    impressora = ImpressaoVisitor()
    visualizador = VisualizacaoVisitor()
    exportador = ExportacaoVisitor()

    # executando imppressão, visualização e exportação
    print("--- Operação de Impressão ---")
    for doc in documentos:
        doc.aceitar(impressora)

    print("\n--- Operação de Visualização ---")
    for doc in documentos:
        doc.aceitar(visualizador)

    print("\n--- Operação de Exportação ---")
    for doc in documentos:
        doc.aceitar(exportador)


if __name__ == "__main__":
    processamento_docs()
