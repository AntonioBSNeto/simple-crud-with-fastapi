# Simple CRUD with FastAPI

Este projeto é um exemplo de uma aplicação CRUD simples utilizando FastAPI.

## Requisitos

- Python 3.8+
- Virtualenv

## Passo a passo para rodar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/simple-crud-with-fastapi.git
cd simple-crud-with-fastapi
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto e adicione a variável `DATABASE_URL` com a URL do seu banco de dados. Exemplo:

```
DATABASE_URL=sqlite:///./test.db
```

### 5. Executar as migrações

```bash
alembic upgrade head
```

### 6. Rodar a aplicação

```bash
uvicorn main:app --reload
```

A aplicação estará disponível em `http://127.0.0.1:8000`.

## Endpoints

### Empresas
- `POST /empresas/` - Cria uma nova empresa
- `GET /empresas/` - Lista todas as empresas
- `GET /empresas/{empresa_id}` - Obtém uma empresa pelo ID
- `DELETE /empresas/{empresa_id}` - Deleta uma empresa pelo ID

### Obrigações Acessórias
- `POST /obrigacoes/` - Cria uma nova obrigação acessória
- `GET /obrigacoes/` - Lista todas as obrigações acessórias
- `GET /obrigacoes/{obrigacao_id}` - Obtém uma obrigação acessória pelo ID
- `DELETE /obrigacoes/{obrigacao_id}` - Deleta uma obrigação acessória pelo ID

## Licença

Este projeto está licenciado sob a licença MIT.