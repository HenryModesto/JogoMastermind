<h1 align="center">🎮 Mastermind Game - API RESTful com Flask + Angular</h1>

<p align="center">
   Aplicação fullstack para o jogo Mastermind
</p>

---

## 📌 Sobre o Projeto

O **Mastermind Game** é uma aplicação **fullstack** desenvolvida utilizando **Angular no frontend** e **Python com Flask no backend**, seguindo o padrão de **API RESTful**.

A aplicação permite que usuários se autentiquem, iniciem partidas do jogo **Mastermind** e tenham suas tentativas registradas em banco de dados, possibilitando também a visualização de um **ranking de jogadores**.

O backend é responsável por:

- autenticação dos usuários
- geração do código secreto
- validação das tentativas
- persistência das partidas
- cálculo de ranking

Já o frontend Angular fornece a interface visual do jogo, com telas de login, dashboard, tabuleiro do jogo e ranking.

### 🧠 Decisões Técnicas Relevantes

- Separação entre **frontend e backend** utilizando arquitetura **API RESTful**.
- Backend estruturado em **camadas (Controller → Service → Repository)** para melhor organização do código.
- O **código secreto do jogo é gerado e mantido apenas no backend**, garantindo integridade das regras do jogo.
- Persistência das partidas e tentativas utilizando banco de dados relacional.
- Comunicação entre Angular e Flask através de **HTTP Requests via Angular Services**.

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python" />
  <img src="https://img.shields.io/badge/Flask-REST%20API-green?logo=flask" />
  <img src="https://img.shields.io/badge/Angular-Frontend-red?logo=angular" />
  <img src="https://img.shields.io/badge/SQLite-Database-lightgrey?logo=sqlite" />
</p>

---

# 📦 Pré-requisitos

Antes de rodar o projeto localmente, é necessário ter instalado:

### Backend

- Python **3.10 ou superior**
- pip

### Frontend

- Node.js **18+**
- npm
- Angular CLI

Instalar Angular CLI:

```bash
npm install -g @angular/cli