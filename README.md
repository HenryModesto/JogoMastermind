# Mastermind Game

## Breve descrição da solução e das decisões técnicas relevantes

Este projeto consiste na implementação do jogo clássico **Mastermind**, utilizando uma arquitetura baseada em **API RESTful**.

A aplicação foi dividida em duas partes principais:

- **Backend:** desenvolvido em **Python utilizando Flask**, responsável pela lógica do jogo, autenticação dos usuários, persistência de dados e exposição dos endpoints da API.
- **Frontend:** desenvolvido em **Angular**, responsável pela interface do usuário, interação com o tabuleiro do jogo e comunicação com a API.

### Principais decisões técnicas

- Utilização de **arquitetura em camadas (Controller → Service → Repository)** no backend para separar responsabilidades.
- Comunicação entre frontend e backend via **API RESTful**.
- Uso de **Angular Services** para centralizar chamadas HTTP para a API.
- Persistência das partidas, tentativas e ranking dos jogadores em banco de dados relacional.
- O **código secreto do jogo é gerado e mantido exclusivamente no backend**, garantindo integridade da lógica do jogo.

---

# Pré-requisitos

Antes de rodar o projeto localmente, é necessário ter instalado:

### Backend

- Python **3.10+**
- pip

### Frontend

- Node.js **18+**
- npm
- Angular CLI

Instalar Angular CLI:

```bash
npm install -g @angular/cli