from AT4_Singleton_Builder_Prototype.Singleton_BD.SistemaFinanceiro import SistemaFinanceiro

if __name__ == "__main__":

    print("SIMULAÇÃO DO SISTEMA FINANCEIRO")

    # O módulo de Relatórios pede a conexão
    sistema_relatorios = SistemaFinanceiro("Módulo de Relatórios")
    sistema_relatorios.conectar_banco()
    sistema_relatorios.gerar_relatorio_financeiro()

    # O módulo de Transações pede a conexão
    sistema_transacoes = SistemaFinanceiro("Módulo de Transações")
    sistema_transacoes.conectar_banco()
    sistema_transacoes.registrar_transacao()

    # O módulo de Relatórios pede novamente (para confirmar que nada novo é criado)
    print("\nMódulo 'Relatórios' pedindo conexão novamente...")
    sistema_relatorios.conectar_banco()

    print("\nVERIFICAÇÃO FINAL DAS INSTÂNCIAS")

    # 8. Verificando se os IDs dos objetos de conexão são os mesmos

    id_conexao_1 = id(sistema_relatorios.conexao)
    id_conexao_2 = id(sistema_transacoes.conexao)

    print(f"ID da conexão em [Relatórios]: {id_conexao_1}")
    print(f"ID da conexão em [Transações]: {id_conexao_2}")

    if id_conexao_1 == id_conexao_2:
        print("\n[SUCESSO] As duas variáveis apontam para a MESMA instância de ConexaoBD.")
        print("O Padrão Singleton foi implementado corretamente!")
    else:
        print("\n[FALHA] As variáveis apontam para instâncias DIFERENTES.")
