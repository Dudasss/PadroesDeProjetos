from PadroesDeProjetos.AT4_Singleton_Builder_Prototype.SingletonBD.ConexaoBD import ConexaoBD


class SistemaFinanceiro:
    def __init__(self, nome_modulo: str):
        self.nome_modulo = nome_modulo
        self.conexao = None
        print(f"Módulo '{self.nome_modulo}' iniciado")

    def conectar_banco(self):
        print(f"[{self.nome_modulo}] Solicitando conexão ao banco de dados...")
        self.conexao = ConexaoBD.getInstance()

    def gerar_relatorio_financeiro(self):
        if self.conexao:
            self.conexao.executar_query("SELECT * FROM relatorio")
        else:
            print(f"[{self.nome_modulo}] Erro: Não há conexão com o banco.")

    def registrar_transacao(self):
        if self.conexao:
            self.conexao.executar_query("INSERT INTO transacoes(valor, tipo) VALUES(200, 'CREDITO')")
        else:
            print(f"[{self.nome_modulo}] Erro: Não há conexão com o banco.")
