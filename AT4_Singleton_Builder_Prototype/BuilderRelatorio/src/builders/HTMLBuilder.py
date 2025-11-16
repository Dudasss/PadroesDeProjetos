from PadroesDeProjetos.AT4_Singleton_Builder_Prototype.BuilderRelatorio.src.Relatorio import Relatorio
from PadroesDeProjetos.AT4_Singleton_Builder_Prototype.BuilderRelatorio.src.builders.RelatorioBuilderInterface import \
    RelatorioBuilderInterface


class HTMLBuilder(RelatorioBuilderInterface):
    def __init__(self):
        self._relatorio = None
        self.reset()

    def reset(self):
        self._relatorio = Relatorio(formato="HTML")

    def add_titulo(self, texto):
        self._relatorio.titulo = f"<h1>{texto}</h1>"

    def add_corpo(self, texto):
        self._relatorio.corpo = f"<p>{texto}</p>"

    def add_graficos(self, dados_grafico):
        self._relatorio.graficos = f"<div>Gráfico com dados: {dados_grafico}</div>"

    def add_rodape(self, texto):
        self._relatorio.rodape = f"<footer>{texto}</footer>"

    def get_relatorio(self):
        # Retorna o relatório final.
        relatorio_final = self._relatorio
        self.reset()
        return relatorio_final

