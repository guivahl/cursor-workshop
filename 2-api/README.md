# Prática 2 — API de Assinaturas

O objetivo é explorar uma API FastAPI real enquanto demonstra recursos do Cursor — não apenas rodar endpoints.

## Como rodar

Requisito: **Python >3.10+**

```bash
cd 2-api
python3 -m venv .venv   # Windows: use python em vez de python3
```

Ative o ambiente virtual:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

Instale as dependências e suba a API:

```bash
pip install -r requirements.txt
uvicorn main:app --reload --app-dir src
```

A API fica em `http://127.0.0.1:8000`. 
Documentação interativa: `http://127.0.0.1:8000/docs`.

## Arquitetura

```
2-api/
├── src/
│   ├── main.py              # App FastAPI, monta routers, /health
│   ├── data/
│   │   └── store.py         # Dados em memória (usuários, planos, assinaturas)
│   ├── schemas/
│   │   └── models.py        # Modelos Pydantic (request/response)
│   ├── services/
│   │   └── subscription.py # Lógica de negócio (preço, assinatura, busca de usuário)
│   └── routers/
│       ├── users.py         # GET /users
│       ├── plans.py         # GET /plans
│       └── subscriptions.py # POST /users/{user_id}/subscribe
├── requirements.txt
└── README.md
```

Fluxo simplificado:

```
src/routers/  →  src/services/  →  src/data/ (memória)
```

- **Rotas** ficam em `src/routers/` — uma pasta por domínio (usuários, planos, assinaturas).
- **Lógica de negócio** fica em `src/services/` — incluindo o cálculo do valor mensal.
- **Dados** ficam em `src/data/` — listas e dicionários em memória, sem banco externo.

## Dados de exemplo

**Usuários:** Ana, Bruno, Carla, Diego (IDs 1–4)

**Planos:**

| ID | Nome | Preço mensal |
|---|---|---|
| 1 | Basic | R$ 29 |
| 2 | Pro | R$ 79 |
| 3 | Enterprise | R$ 199 |
