class ConexaoBD:
    _instance = None  # var da instancia unica

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print('Instância não encontrada. Criando nova conexão...')
            cls._instance = super().__new__(cls)
        else:
            print('Instância já existe. Retornando conexão atual.')
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            print(f"Configurando conexão pela primeira vez... (ID: {id(self)}")

            # Simulando a configuração da conexão
            self.connection_info = 'Conecatando ao BD.'
            self.id_obj = id(self)

            self.intialized = True
        else:
            print(f"Conexão já estava configurada. (ID: {id(self)}")

    @classmethod
    def getInstance(cls):
        print("Chamando ConexaoBD.")
        return cls()

    #  métodos de simulação
    def executar_query(self, query):
        print(f"[Conexão {self.id_obj}]: executando query: '{query}'")

    def fechar_conexao(self):
        print(f"[Conexão {self.id_obj}]: encerrada.")
