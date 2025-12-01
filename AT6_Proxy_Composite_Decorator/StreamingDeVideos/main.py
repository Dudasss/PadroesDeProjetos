from PadroesDeProjetos.AT6_Proxy_Composite_Decorator.StreamingDeVideos.Proxy.ProxyVideo import ProxyVideo


def main():
    print("--- Teste 1: Usuário Visitante (Não Autenticado) ---")
    usuario_visitante = {'nome': 'Ana', 'autenticado': False}
    proxy_filme1 = ProxyVideo("Matrix", usuario_visitante)

    # Tentando assistir
    proxy_filme1.exibir()

    print("\n--- Teste 2: Usuário Premium (Autenticado) ---")
    usuario_premium = {'nome': 'Beto', 'autenticado': True}
    proxy_filme2 = ProxyVideo("Interestelar", usuario_premium)

    # Tentando assistir (Vai carregar do disco)
    proxy_filme2.exibir()

    print("\n--- Teste 3: Segunda execução do mesmo filme (Cache) ---")
    # Não deve carregar do disco novamente, pois já está em memória
    proxy_filme2.exibir()


if __name__ == "__main__":
    main()
