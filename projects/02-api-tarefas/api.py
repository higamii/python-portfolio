"""API REST de tarefas (armazenamento em memória)."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API de Tarefas", version="1.0.0")


class TarefaIn(BaseModel):
    titulo: str
    concluida: bool = False


class Tarefa(TarefaIn):
    id: int


_tarefas: dict[int, Tarefa] = {}
_estado = {"proximo_id": 1}


def _buscar(tarefa_id: int) -> Tarefa:
    if tarefa_id not in _tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return _tarefas[tarefa_id]


@app.get("/tarefas", response_model=list[Tarefa])
def listar():
    return list(_tarefas.values())


@app.post("/tarefas", response_model=Tarefa, status_code=201)
def criar(dados: TarefaIn):
    tarefa = Tarefa(id=_estado["proximo_id"], **dados.model_dump())
    _tarefas[tarefa.id] = tarefa
    _estado["proximo_id"] += 1
    return tarefa


@app.get("/tarefas/{tarefa_id}", response_model=Tarefa)
def obter(tarefa_id: int):
    return _buscar(tarefa_id)


@app.put("/tarefas/{tarefa_id}", response_model=Tarefa)
def atualizar(tarefa_id: int, dados: TarefaIn):
    _buscar(tarefa_id)
    tarefa = Tarefa(id=tarefa_id, **dados.model_dump())
    _tarefas[tarefa_id] = tarefa
    return tarefa


@app.delete("/tarefas/{tarefa_id}", status_code=204)
def remover(tarefa_id: int):
    _buscar(tarefa_id)
    del _tarefas[tarefa_id]
