from abc import ABC, abstractmethod


class RelatorioBuilderInterface(ABC):
    @abstractmethod
    def reset(self):
        # Prepara um novo objeto de relatório em branco.
        pass

    @abstractmethod
    def add_titulo(self, texto):
        pass

    @abstractmethod
    def add_corpo(self, texto):
        self

    @abstractmethod
    def add_graficos(self, dados_grafico):
        pass

    @abstractmethod
    def add_rodape(self, texto):
        pass

    @abstractmethod
    def get_relatorio(self):
        # Retorna o relatório final.
        pass
