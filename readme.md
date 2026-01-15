# FastAPI CRUD - To do

API CRUD simples desenvolvida com Python e FastAPI, com operações básicas
de criação, leitura, atualização e remoção de registros.

_____________
🛠 Tecnologias:
- Python 3.14
- FastAPI
- Uvicorn
- Pydantic


## ▶️ Como executar o projeto

1. Clone o repositório

2. Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```


3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação:

```bash
uvicorn main:app --reload
```

## 🧪 Como testar a API
1. Após iniciar a aplicação, acesse a documentação interativa:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

Nessas páginas é possível visualizar todos os endpoints disponíveis,
seus parâmetros, modelos de request/response e testá-los diretamente.