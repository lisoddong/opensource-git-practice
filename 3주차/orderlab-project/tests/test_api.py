import pytest
from fastapi.testclient import TestClient

from orderlab.api import create_app


@pytest.fixture
def client():
    with TestClient(create_app()) as test_client:
        yield test_client


def test_create_and_get(client):
    response = client.post("/orders", json={"price": 10_000, "quantity": 2})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "subtotal": 20_000}
    retrieved = client.get("/orders/1")
    assert retrieved.status_code == 200
    assert retrieved.json() == response.json()


@pytest.mark.parametrize(
    "payload, field",
    [
        ({"price": 100, "quantity": 0}, "quantity"),
        ({"price": 100, "quantity": -1}, "quantity"),
        ({"price": -1, "quantity": 1}, "price"),
        ({"price": "bad", "quantity": 1}, "price"),
        ({"quantity": 1}, "price"),
    ],
)
def test_invalid_order(client, payload, field):
    response = client.post("/orders", json=payload)
    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", field]
    assert client.get("/orders/1").status_code == 404


def test_not_found(client):
    response = client.get("/orders/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not found"}


def test_zero_price(client):
    response = client.post("/orders", json={"price": 0, "quantity": 1})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "subtotal": 0}


def test_separate_orders(client):
    first = client.post("/orders", json={"price": 100, "quantity": 2})
    second = client.post("/orders", json={"price": 300, "quantity": 3})
    assert first.json() == {"id": 1, "subtotal": 200}
    assert second.json() == {"id": 2, "subtotal": 900}
    assert client.get("/orders/1").json() == first.json()
    assert client.get("/orders/2").json() == second.json()


def test_apps_do_not_share_state(client):
    client.post("/orders", json={"price": 100, "quantity": 1})
    with TestClient(create_app()) as other:
        assert other.get("/orders/1").status_code == 404
        created = other.post("/orders", json={"price": 50, "quantity": 1})
        assert created.json() == {"id": 1, "subtotal": 50}
    assert client.get("/orders/1").json() == {"id": 1, "subtotal": 100}
