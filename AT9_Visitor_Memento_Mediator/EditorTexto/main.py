from AT9_Visitor_Memento_Mediator.EditorTexto.Classes.Documento import Documento
from AT9_Visitor_Memento_Mediator.EditorTexto.Classes.Editor import Editor


def SistemaEditorTexto():
    doc_inicial = Documento()
    editor = Editor(doc_inicial)

    editor.escrever_e_salvar("Versão 1 do documento.")
    editor.escrever_e_salvar("Versão 2 do documento.")
    editor.escrever_e_salvar("Versão 3 do documento.")

    # Iniciando os Undos
    editor.desfazer()  # Volta para V2
    editor.desfazer()  # Volta para V1
    editor.desfazer()  # Esvazia/Estado inicial


if __name__ == "__main__":
    SistemaEditorTexto()
