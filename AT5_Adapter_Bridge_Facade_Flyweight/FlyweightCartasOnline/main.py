from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.FlyweightCartasOnline.Classes.Jogador import Jogador


def main():
    print("--- Início do Jogo de Cartas (Flyweight) ---\n")

    jogador1 = Jogador("Ana")
    jogador2 = Jogador("Bruno")

    # Ana recebe um Ás de Espadas (Criação Nova)
    jogador1.receber_carta("Ás", "Espadas")

    # Bruno recebe um Ás de Espadas (Reutilização!)
    jogador2.receber_carta("Ás", "Espadas")

    # Ambos recebem outras cartas
    jogador1.receber_carta("Rei", "Copas")
    jogador2.receber_carta("Rei", "Copas")

    print("\n--- Verificação de Identidade de Objeto ---")

    # Pegamos as referências das cartas
    carta_ana = jogador1.mao[0]  # Ás de Espadas
    carta_bruno = jogador2.mao[0]  # Ás de Espadas

    print(f"Carta da Ana: {carta_ana} (ID Memória: {id(carta_ana)})")
    print(f"Carta do Bruno: {carta_bruno} (ID Memória: {id(carta_bruno)})")

    if carta_ana is carta_bruno:
        print(">> SUCESSO: Ambas as variáveis apontam para o MESMO objeto na memória.")
    else:
        print(">> FALHA: Objetos diferentes foram criados.")


if __name__ == "__main__":
    main()
