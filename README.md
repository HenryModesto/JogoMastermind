# Mastermind Game (Angular + Flask)

Este projeto consiste na implementação do clássico jogo **Mastermind**, utilizando uma arquitetura moderna baseada em **API RESTful**.

O sistema é dividido em duas aplicações principais:

- **Frontend:** Angular
- **Backend:** Python + Flask
- **Banco de dados:** SQLite 

O objetivo do jogo é adivinhar uma combinação secreta gerada pelo sistema dentro de **10 tentativas**, recebendo feedback a cada tentativa sobre quantos valores estão corretos.

---

# 📌 Descrição do Projeto

O sistema permite que usuários se autentiquem, iniciem partidas do jogo Mastermind e tenham seu desempenho registrado em um ranking.

Cada partida gera um código secreto que deve ser descoberto pelo jogador. A cada tentativa, o backend valida o palpite e retorna apenas o número de posições corretas.

O sistema registra:

- histórico das partidas
- tentativas realizadas
- pontuação dos jogadores
- ranking geral

---

# 🏗 Arquitetura

O backend segue uma arquitetura em camadas baseada no padrão:
      
Controller → Service → Repository

Essa estrutura separa responsabilidades e melhora a organização do código.
