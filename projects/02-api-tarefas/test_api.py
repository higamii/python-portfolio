import pytest
from fastapi.testclient import TestClient

import api

client = TestClient(api.app)


@pytest.fixture(autouse=True)
def limpar_estado():
    api._tarefas.clear()
    api._estado["proximo_id"] = 1


def test_criar_e_listar():
    r = client.post("/tarefas", json={"titulo": "Estudar Python"})
    assert r.status_code == 201
    assert r.json() == {"id": 1, "titulo": "Estudar Python", "concluida": False}
    assert len(client.get("/tarefas").json()) == 1


def test_atualizar():
    client.post("/tarefas", json={"titulo": "A"})
    r = client.put("/tarefas/1", json={"titulo": "A", "concluida": True})
    assert r.json()["concluida"] is True


def test_remover():
    client.post("/tarefas", json={"titulo": "A"})
    assert client.delete("/tarefas/1").status_code == 204
    assert client.get("/tarefas/1").status_code == 404


def test_validacao():
    assert client.post("/tarefas", json={}).status_code == 422
