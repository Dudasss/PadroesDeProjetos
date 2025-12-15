from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.AtendimentoClienteChainResponsibility.Classes.TipoSolicitacao import \
    TipoSolicitacao


class Solicitacao:
    def __init__(self, tipo: TipoSolicitacao, conteudo: str):
        self.tipo = tipo
        self.conteudo = conteudo

    def __str__(self):
        return self.conteudo
