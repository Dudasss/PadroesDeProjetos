from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.AtendimentoClienteChainResponsibility.Classes import Solicitacao
from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.AtendimentoClienteChainResponsibility.Classes.TipoSolicitacao import \
    TipoSolicitacao
from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.AtendimentoClienteChainResponsibility.Interface.AtendenteInterface import \
    AtendenteInterface


class AtendenteConsulta(AtendenteInterface):
    def processar(self, solicitacao: Solicitacao) -> None:
        if solicitacao.tipo == TipoSolicitacao.CONSULTA:
            print(f"Atendente de Consulta: {solicitacao.conteudo}")
        else:
            self.passar_adiante(solicitacao)
