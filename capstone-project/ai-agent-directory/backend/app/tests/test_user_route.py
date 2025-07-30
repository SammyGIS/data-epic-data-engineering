import os
import sys
import uuid
from datetime import datetime
from fastapi import FastAPI, status
from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.database import Base, get_db
from core.models.user import User
from api.route.user import user_router  # <-- Adjust if your import path is different

TEST_SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def test_db():
    connection = engine.connect()
    transaction = connection.begin()
    Base.metadata.create_all(bind=connection)
    session = TestingSessionLocal(bind=connection)

    # Insert a sample user for testing
    sample_user = User(
        id=uuid.uuid4(),
        first_name="John",
        last_name="Doe",
        username="johndoe",
        email="john@example.com",
        hashed_password="fakehashedpassword",
        is_admin=0,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    session.add(sample_user)
    session.commit()

    yield session

    session.close()
    transaction.rollback()
    connection.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def test_app(test_db):
    app = FastAPI()
    app.include_router(user_router, prefix="/users")

    # Override get_db dependency to use test_db session
    def override_get_db():
        yield test_db

    app.dependency_overrides[get_db] = override_get_db

    return app


@pytest.fixture(scope="function")
def client(test_app):
    with TestClient(test_app) as c:
        yield c


def test_get_user_by_id(client, test_db):
    user_in_db = test_db.query(User).first()
    response = client.get(f"/users/{user_in_db.id}")

    assert response.status_code == 200
    data = response.json()
    assert data["username"] == user_in_db.username
    assert data["email"] == user_in_db.email


def test_get_user_not_found(client):
    fake_id = str(uuid.uuid4())
    response = client.get(f"/users/{fake_id}")

    assert response.status_code == 404
    # Accept either generic or custom message
    assert response.json().get("detail") in ["User not found", "Not Found"]


def test_create_user(client):
    payload = {
        "first_name": "Alice",
        "last_name": "Smith",
        "username": "alicesmith",
        "email": "alice@example.com",
        "password": "securepassword123"
    }

    response = client.post("/users/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]

def test_update_user_not_found(client):
    fake_id = str(uuid.uuid4())
    update_payload = {
        "first_name": "Nobody",
        "last_name": "Nowhere",
        "email": "nobody@example.com"
    }
    response = client.put(f"/users/{fake_id}", json=update_payload)
    assert response.status_code == 404
    assert response.json().get("detail") in ["User not found", "Not Found"]
