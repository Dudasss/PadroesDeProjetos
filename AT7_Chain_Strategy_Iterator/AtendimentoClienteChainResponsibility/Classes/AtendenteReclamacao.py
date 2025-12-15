from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.AtendimentoClienteChainResponsibility.Classes import Solicitacao
from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.AtendimentoClienteChainResponsibility.Classes.TipoSolicitacao import \
    TipoSolicitacao
from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.AtendimentoClienteChainResponsibility.Interface.AtendenteInterface import \
    AtendenteInterface


class AtendenteReclamacao(AtendenteInterface):
    def processar(self, solicitacao: Solicitacao) -> None:
        if solicitacao.tipo == TipoSolicitacao.RECLAMACAO:
            print(f"Atendente de Reclamação: {solicitacao.conteudo}")
        else:
            self.passar_adiante(solicitacao)
