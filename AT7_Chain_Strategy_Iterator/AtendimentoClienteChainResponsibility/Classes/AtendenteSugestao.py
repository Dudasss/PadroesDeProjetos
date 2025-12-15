from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.AtendimentoClienteChainResponsibility.Classes import Solicitacao
from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.AtendimentoClienteChainResponsibility.Classes.TipoSolicitacao import \
    TipoSolicitacao
from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.AtendimentoClienteChainResponsibility.Interface.AtendenteInterface import \
    AtendenteInterface


class AtendenteSugestao(AtendenteInterface):
    def processar(self, solicitacao: Solicitacao) -> None:
        if solicitacao.tipo == TipoSolicitacao.SUGESTAO:
            print(f"Atendente de Sugestão: {solicitacao.conteudo}")
        else:
            self.passar_adiante(solicitacao)
