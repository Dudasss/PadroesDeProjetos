from PadroesDeProjetos.AT4_Singleton_Builder_Prototype.BuilderRelatorio.src.Relatorio import Relatorio
from PadroesDeProjetos.AT4_Singleton_Builder_Prototype.BuilderRelatorio.src.builders.RelatorioBuilderInterface import \
    RelatorioBuilderInterface


class WordBuilder(RelatorioBuilderInterface):
    def __init__(self):
        self._relatorio = None
        self.reset()

    def reset(self):
        self._relatorio = Relatorio(formato="Word")

    def add_titulo(self, texto):
        self._relatorio.titulo = f"**{texto.upper()}**"

    def add_corpo(self, texto):
        self._relatorio.corpo = f"{texto}"

    def add_graficos(self, dados_grafico):
        self._relatorio.graficos = f"Imagem: [Gráfico {dados_grafico}]"

    def add_rodape(self, texto):
        self._relatorio.rodape = f"(c) {texto}"

    def get_relatorio(self):
        # Retorna o relatório final.
        relatorio_final = self._relatorio
        self.reset()
        return relatorio_final

