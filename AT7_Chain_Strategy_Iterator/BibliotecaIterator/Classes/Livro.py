from dataclasses import dataclass


@dataclass
class Livro:
    titulo: str
    autor: str

    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}"
