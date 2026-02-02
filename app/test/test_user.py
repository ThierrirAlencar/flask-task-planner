import pytest
from app.core.database import db
from app.server import create_app


# Um mock do banco de dados utilizando um in_memory
@pytest.fixture
def app():
    test_config = {"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"}
    app = create_app(test_config=test_config)

    with app.app_context():
        # create_app already initialized db and called create_all using the provided test config
        yield app
        # teardown
        db.drop_all()

# Pra fazer testesm na api é nescessário definir um fixture para o cliente, o flask possui uma instância test_client
@pytest.fixture
def client(app):
    return app.test_client()


def test_create_user(client):
    payload = {"name": "Alice", "email": "alice@example.com", "password": "secret"}
    resp = client.post("/users/", json=payload)
    assert resp.status_code in (200, 201)
    data = resp.get_json()
    assert "id" in data
    assert data["name"] == "Alice"


def test_get_user(client):
    # create
    payload = {"name": "Bob", "email": "bob@example.com", "password": "pwd"}
    resp = client.post("/users/", json=payload)
    u = resp.get_json()
    user_id = u["id"]

    # get
    resp = client.get(f"/users/single/{user_id}")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["id"] == user_id
    assert data["name"] == "Bob"
    assert data["email"] == "bob@example.com"


def test_update_user(client):
    # create
    payload = {"name": "Carol", "email": "carol@example.com", "password": "pwd"}
    resp = client.post("/users/", json=payload)
    user_id = resp.get_json()["id"]

    # update email
    update_payload = {"email": "newcarol@example.com"}
    resp = client.put(f"/users/update/{user_id}", json=update_payload)
    # endpoint should return a success code (200 or 204)
    assert resp.status_code in (200, 204)

    # confirm change
    resp = client.get(f"/users/single/{user_id}")
    data = resp.get_json()
    # NOTE: if this assertion fails, the update implementation has a bug
    assert data["email"] == "newcarol@example.com"


def test_delete_user(client):
    # create
    payload = {"name": "Dan", "email": "dan@example.com", "password": "pwd"}
    resp = client.post("/users/", json=payload)
    user_id = resp.get_json()["id"]

    # delete
    resp = client.delete(f"/users/delete/{user_id}")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data.get("deleted") is True

    # confirm not found
    resp = client.get(f"/users/single/{user_id}")
    assert resp.status_code == 404
