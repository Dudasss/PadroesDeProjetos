from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.FacadeCinemaOnline.Classes.SistemaAuth import SistemaAuth
from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.FacadeCinemaOnline.Classes.SistemaPagamento import \
    SistemaPagamento
from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.FacadeCinemaOnline.Classes.SistemaReproducao import \
    SistemaReproducao


class CinemaFacade:
    def __init__(self):
        # a fachada irá inicializar os sistemas necessários
        self.auth = SistemaAuth()
        self.pagamento = SistemaPagamento()
        self.play = SistemaReproducao()

    def assistir_filme(self, usuario: str, filme: str, valor: float) -> None:
        print(f"Iniciando sessão para {usuario}")

        if self.auth.login(usuario):
            if self.pagamento.processar_pagamento(valor):
                self.play.reproduzir_video(filme)
                print("Sessão conluida.")
            else:
                print("Erro: Pagamento falhou.")
        else:
            print("Erro: Autenticação falhou.")
