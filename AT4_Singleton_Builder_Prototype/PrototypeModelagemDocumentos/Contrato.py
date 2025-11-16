import copy

from PadroesDeProjetos.AT4_Singleton_Builder_Prototype.PrototypeModelagemDocumentos.DocumentoPrototipo import \
    DocumentoPrototipo


class Contrato(DocumentoPrototipo):
    def __init__(self, titulo: str, corpo: str, clausulas: list[str], rodape: str):
        self.titulo = titulo
        self.corpo = corpo
        self.clausulas = clausulas
        self.rodape = rodape

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        clausulas_txt = "\n".join([f"-{c}" for c in self.clausulas])
        return (
            f"{self.titulo.upper()}\n"
            f"{self.corpo}\n"
            f"Cláusulas: \n{self.clausulas}\n"
            f"Rodapé: {self.rodape}"
        )