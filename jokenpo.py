def jokenpo():
    opcoes = ("pedra", "papel", "tesoura")

    while True:
        print("""
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        Escolha pedra, papel ou tesoura
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """)

        jogador1 = input("Jogador 1: ").strip().lower()
        while jogador1 not in opcoes:
            print("Opção inválida! Tente novamente.")
            jogador1 = input("Jogador 1: ").strip().lower()

        jogador2 = input("Jogador 2: ").strip().lower()
        while jogador2 not in opcoes:
            print("Opção inválida! Tente novamente.")
            jogador2 = input("Jogador 2: ").strip().lower()

        resultado = "Empate!" if jogador1 == jogador2 else \
                    "Jogador 1 venceu!" if (jogador1, jogador2) in [("pedra", "tesoura"), ("tesoura", "papel"), ("papel", "pedra")] else \
                    "Jogador 2 venceu!"

        print(f"""
        Jogador 1: {jogador1}
        Jogador 2: {jogador2}
        Resultado: {resultado}
        """)

        if input("Jogar novamente? (s/n): ").strip().lower() != "s":
            break

jokenpo()
