from PadroesDeProjetos.AT4_Singleton_Builder_Prototype.BuilderRelatorio.src.builders.RelatorioBuilderInterface import \
    RelatorioBuilderInterface


class Director:
    def __init__(self):
        self._builder = None

    def set_builder(self, builder: RelatorioBuilderInterface):
        self._builder = builder

    def construir_relatorio_completo(self, dados=None):
        # criar um relatorio com todas as seções
        if not self._builder:
            raise ValueError("Builder não definido.")

        self._builder.reset()
        self._builder.add_titulo(dados['titulo'])
        self._builder.add_corpo(dados['corpo'])
        self._builder.add_graficos(dados['graficos'])
        self._builder.add_rodape(dados['rodape'])

    def construir_relatorio_resumido(self, dados=None):
        # criar um relatorio sem gráficos
        if not self._builder:
            raise ValueError("Builder não definido.")

        self._builder.reset()
        self._builder.add_titulo(dados['titulo'])
        self._builder.add_corpo(dados['corpo'])
        self._builder.add_rodape(dados['rodape'])

