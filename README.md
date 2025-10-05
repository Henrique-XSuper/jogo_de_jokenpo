# Jogo Jokenpô (Pedra, Papel, Tesoura)
Este é um jogo de Jokenpô simples, onde dois jogadores podem competir no clássico "pedra, papel ou tesoura" através do terminal. O programa continua executando até que os jogadores decidam parar.

---
## 🔎 Funcionalidades.
- Jogo de Dois Jogadores: Permite que dois jogadores insiram suas jogadas para competir.
- Loop de Jogo: O jogo continua em um loop, permitindo várias rodadas sem a necessidade de reiniciar o programa.
- Validação de Entrada: Garante que apenas as opções válidas ("pedra", "papel", "tesoura") sejam aceitas como entrada.
- Regras Clássicas: Implementa as regras tradicionais do Jokenpô para determinar o vencedor.
- Interface Simples: Usa o console para uma experiência de jogo direta e clara.

---
## ⚙️Requisitos
Python 3 instalado.
GoogleColab, júpiter ou vs code/vs Studio 

---
## 🧠Lógica do Código
1. O jogo é executado dentro de uma função jokenpo() que contém um while loop para permitir múltiplas rodadas.
2. Um tuple chamado opcoes armazena as escolhas válidas para os jogadores.
3. As jogadas dos jogador1 e jogador2 são coletadas e validadas, garantindo que estejam dentro das opções aceitas.
4. A lógica para determinar o vencedor usa uma expressão ternária aninhada, que é uma forma compacta de verificar todas as combinações possíveis de vitórias e empates.
5. O resultado é exibido na tela, e o programa pergunta se os jogadores querem continuar.
