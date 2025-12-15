from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.AtendimentoClienteChainResponsibility.Classes.AtendenteConsulta import \
    AtendenteConsulta
from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.AtendimentoClienteChainResponsibility.Classes.AtendenteReclamacao import \
    AtendenteReclamacao
from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.AtendimentoClienteChainResponsibility.Classes.AtendenteSugestao import \
    AtendenteSugestao
from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.AtendimentoClienteChainResponsibility.Classes.Solicitacao import \
    Solicitacao
from PadroesDeProjetos.AT7_Chain_Strategy_Iterator.AtendimentoClienteChainResponsibility.Classes.TipoSolicitacao import \
    TipoSolicitacao


def atendimento_cliente():
    consulta = AtendenteConsulta()
    reclamacao = AtendenteReclamacao()
    sugestao = AtendenteSugestao()

    # Configurando a cadeia (Chain)
    # Consulta -> Reclamação -> Sugestão
    consulta.definir_proximo(reclamacao).definir_proximo(sugestao)

    solicitacoes = [
        Solicitacao(TipoSolicitacao.SUGESTAO, "Sugiro que aumentem o horário de atendimento."),
        Solicitacao(TipoSolicitacao.CONSULTA, "Qual é o horário de funcionamento?"),
        Solicitacao(TipoSolicitacao.RECLAMACAO, "Nenhum produto veio danificado."),
        Solicitacao(TipoSolicitacao.OUTRO, "Quero falar com o Comercial.")
    ]

    print("INICIANDO OS ATENDIMENTOS")

    for sol in solicitacoes:
        consulta.processar(sol)


if __name__ == "__main__":
    atendimento_cliente()
