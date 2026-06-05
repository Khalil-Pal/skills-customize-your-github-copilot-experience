from fastapi.testclient import TestClient
import importlib.util
import os

spec = importlib.util.spec_from_file_location(
    "fastapi_app",
    os.path.join(os.path.dirname(__file__), "..", "main.py"),
)
app_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app_mod)
app = app_mod.app
client = TestClient(app)


def test_create_and_get_item():
    res = client.post("/items/", json={"name": "Widget", "description": "A useful widget", "price": 9.99})
    assert res.status_code == 201
    data = res.json()
    assert data["id"] == 1

    res2 = client.get(f"/items/{data['id']}")
    assert res2.status_code == 200
    assert res2.json()["name"] == "Widget"


def test_delete_requires_auth():
    res = client.post("/items/", json={"name": "ToDelete", "description": "temp", "price": 2.0})
    assert res.status_code == 201
    item_id = res.json()["id"]

    res = client.delete(f"/items/{item_id}")
    assert res.status_code == 401

    res = client.delete(f"/items/{item_id}", headers={"x-api-key": "secret"})
    assert res.status_code == 204
