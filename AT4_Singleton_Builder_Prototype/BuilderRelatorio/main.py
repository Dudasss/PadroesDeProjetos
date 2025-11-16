from PadroesDeProjetos.AT4_Singleton_Builder_Prototype.BuilderRelatorio.src.Director import Director
from PadroesDeProjetos.AT4_Singleton_Builder_Prototype.BuilderRelatorio.src.builders.HTMLBuilder import HTMLBuilder
from PadroesDeProjetos.AT4_Singleton_Builder_Prototype.BuilderRelatorio.src.builders.PDFBuilder import PDFBuilder
from PadroesDeProjetos.AT4_Singleton_Builder_Prototype.BuilderRelatorio.src.builders.WordBuilder import WordBuilder

if __name__ == "__main__":
    dados_relatorio = {
        'titulo': "Relatório De Vendas Semestral.",
        'corpo': "Este é o conteúdo do 'Relatório De Vendas Semestral'...",
        'graficos': "['vendas mensais', vendas semanais]",
        'rodape': "IFBA Irecê - 2025."
    }

    # Criar o director
    director = Director()

    # Criar builders
    pdf_builder = PDFBuilder()
    html_builder = HTMLBuilder()
    word_builder = WordBuilder()
    print(f"{'-' * 40}")
    # Criar relatório COMPLETO PDF
    print("RELATÓRIO EM PDF")
    director.set_builder(pdf_builder)  # DEFINIR BUILDER
    director.construir_relatorio_completo(dados_relatorio)  # CONTRUIR RELATORIO
    relatorio_pdf = pdf_builder.get_relatorio()  # PEGAR O RELATORIO
    print(relatorio_pdf)
    print(f"{'-'*40}")

    # Criar relatório COMPLETO HTML
    print("RELATÓRIO EM HTML")
    director.set_builder(html_builder)  # DEFINIR BUILDER
    director.construir_relatorio_completo(dados_relatorio)  # CONTRUIR RELATORIO
    relatorio_html = html_builder.get_relatorio()  # PEGAR O RELATORIO
    print(relatorio_html)
    print(f"{'-' * 20}")

    # Criar relatório PARCIAL EM WORD
    print("RELATÓRIO EM WORD")
    director.set_builder(word_builder)  # DEFINIR BUILDER
    director.construir_relatorio_resumido(dados_relatorio)  # CONTRUIR RELATORIO
    relatorio_word = word_builder.get_relatorio()  # PEGAR O RELATORIO
    print(relatorio_word)
    print(f"{'-' * 20}")

    # Criar relatório manual em WORD (SEM BUILDER)
    print("RELATÓRIO MANUAL EM WORD")
    word_builder.reset()
    word_builder.add_titulo("Relatório Manul em Word.")
    word_builder.add_rodape("Dudasss Inc")
    relatorio_word_manual = word_builder.get_relatorio()
    print(relatorio_word_manual)
    print(f"{'-' * 20}")
