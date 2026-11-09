# 02 · API de Tarefas

CRUD de tarefas com **FastAPI** e validação via **pydantic**.

## Executar
```bash
uvicorn api:app --reload
```
Documentação interativa: http://127.0.0.1:8000/docs

## Endpoints
| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/tarefas` | Lista tarefas |
| POST | `/tarefas` | Cria tarefa |
| GET | `/tarefas/{id}` | Busca tarefa |
| PUT | `/tarefas/{id}` | Atualiza tarefa |
| DELETE | `/tarefas/{id}` | Remove tarefa |

## Testes
```bash
pytest
```

## Próximos passos
- Trocar o armazenamento em memória por SQLite/SQLAlchemy
- Autenticação com JWT
- Dockerfile
