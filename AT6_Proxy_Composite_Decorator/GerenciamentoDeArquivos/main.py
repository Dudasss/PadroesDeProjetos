from AT6_Proxy_Composite_Decorator.GerenciamentoDeArquivos.Classes.Arquivo import Arquivo
from AT6_Proxy_Composite_Decorator.GerenciamentoDeArquivos.Composite.Pasta import Pasta


def main():
    print("--- Criando Estrutura de Arquivos ---")

    # 1. Criando a Raiz
    raiz = Pasta("Projetos")

    # 2. Criando Subpastas
    pasta_front = Pasta("FrontEnd")
    pasta_back = Pasta("BackEnd")

    # 3. Criando Arquivos
    arq1 = Arquivo("index.html")
    arq2 = Arquivo("style.css")
    arq3 = Arquivo("api.py")
    arq4 = Arquivo("db_config.json")

    # 4. Montando a Árvore (Composite)
    pasta_front.adicionar(arq1)
    pasta_front.adicionar(arq2)

    pasta_back.adicionar(arq3)
    pasta_back.adicionar(arq4)

    raiz.adicionar(pasta_front)
    raiz.adicionar(pasta_back)

    # 5. Exibindo a Estrutura Completa
    print("\nVisualização da Hierarquia:")
    raiz.exibir()

    # 6. Removendo um arquivo
    print("\n--- Removendo 'style.css' ---")
    pasta_front.remover(arq2)
    raiz.exibir()


if __name__ == "__main__":
    main()