# Projeto MVC em Python

Este é um projeto de exemplo que demonstra a arquitetura Model-View-Controller (MVC) utilizando Python. O objetivo é fornecer uma estrutura clara e organizada para o desenvolvimento de aplicações, separando as responsabilidades em três componentes principais:

- **Model (Modelo):** Responsável pela lógica de negócios e manipulação de dados. Interage diretamente com o banco de dados e define a estrutura dos dados.
- **View (Visão):** Responsável pela apresentação dos dados ao usuário. Neste projeto, as "views" são representadas pelas classes que formatam as respostas HTTP.
- **Controller (Controlador):** Atua como intermediário entre o Modelo e a Visão. Recebe as requisições do usuário, processa-as, interage com o Modelo para obter ou manipular dados e, em seguida, seleciona a Visão apropriada para exibir a resposta.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
src/
├── controllers/        # Lógica de controle e orquestração
├── errors/             # Tratamento de erros personalizados
├── main/               # Configurações principais (rotas, servidor, compositores)
├── models/             # Modelos de dados e lógica de interação com o banco de dados
└── views/              # Formatação das respostas HTTP
```

## Como Executar

Para executar este projeto, siga os passos abaixo:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/thiagonmiziara/mvc.git
   cd mvc
   ```

2. **Crie e ative um ambiente virtual (recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Linux/macOS
   # venv\Scripts\activate   # No Windows
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**
   ```bash
   python run.py
   ```

A aplicação estará disponível em `http://localhost:3000` (ou na porta configurada).

## Tecnologias Utilizadas

- **Python:** Linguagem de programação principal.
- **SQLite:** Banco de dados leve e embutido para persistência de dados.
- **Pylint:** Ferramenta de análise estática de código para garantir a qualidade.
- **Pre-commit:** Hooks para automatizar a verificação de código antes dos commits.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias, correções de bugs ou novas funcionalidades.
