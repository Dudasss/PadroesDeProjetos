from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.BibliotecaIterator.Classes.Biblioteca import Biblioteca
from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.BibliotecaIterator.Classes.Livro import Livro


def sistema_biblioteca():
    biblioteca = Biblioteca()
    biblioteca.adicionar_livro(Livro("1984", "George Orwell"))
    biblioteca.adicionar_livro(Livro("O Senhor dos Anéis", "J.R.R. Tolkien"))
    biblioteca.adicionar_livro(Livro("Dom Casmurro", "Machado de Assis"))

    # Uso do Iterator
    print("--- Lista de Livros na Biblioteca ---")
    iterator = biblioteca.create_iterator()

    # Loop manual usando o padrão Iterator (while has_next)
    while iterator.has_next():
        # atual = iterator.current_item()
        # print(f"Espiando o atual: {atual.titulo}")
        livro = iterator.next()
        print(livro)


if __name__ == "__main__":
    sistema_biblioteca()