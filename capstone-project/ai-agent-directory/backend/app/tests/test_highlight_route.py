import os
import sys
import uuid
from datetime import datetime

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi_pagination import add_pagination
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Adjust path to import your app modules properly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Set environment variables for test config
os.environ["DATABASE_URL"] = "sqlite://"
os.environ["TESTING"] = "true"

from auth.dependency import get_current_user
from core.database import Base, get_db
from core.models.highlight import Highlight
from core.models.user import User
from api.route.highlight import highlight_router  # Your highlight router

# Use a fixed UUID for testing user consistency
TEST_USER_ID = uuid.UUID("12345678-1234-5678-1234-567812345678")

# Create a SQLite in-memory DB for tests
TEST_SQLALCHEMY_DATABASE_URL = "sqlite://"
test_engine = create_engine(
    TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=test_engine
)


@pytest.fixture(scope="function")
def test_session():
    connection = test_engine.connect()
    transaction = connection.begin()
    Base.metadata.create_all(bind=connection)

    session = TestingSessionLocal(bind=connection)

    # Add a test user for foreign key reference
    test_user = User(
        id=TEST_USER_ID,
        first_name="Test",
        last_name="User",
        username="testuser",
        email="test@example.com",
        hashed_password="fakehashed",
        is_admin=0,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    session.add(test_user)
    session.commit()

    yield session

    session.close()
    transaction.rollback()
    connection.close()
    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(scope="function")
def test_app():
    app = FastAPI()
    app.include_router(highlight_router, prefix="/api")
    add_pagination(app)
    return app


@pytest.fixture(scope="function")
def client(test_session, test_app):
    def override_get_db():
        yield test_session

    def mock_get_current_user():
        return User(
            id=TEST_USER_ID,
            first_name="Test",
            last_name="User",
            username="testuser",
            email="test@example.com",
            hashed_password="fakehashed",
            is_admin=0,
        )

    test_app.dependency_overrides[get_db] = override_get_db
    test_app.dependency_overrides[get_current_user] = mock_get_current_user

    with TestClient(test_app) as c:
        yield c

    test_app.dependency_overrides.clear()


def test_save_highlight(client):
    payload = {"agent_name": "Jasper.ai"}
    response = client.post("/api/highlights/Jasper.ai", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["agent_name"] == "Jasper.ai"
    assert "id" in data


def test_save_highlight_duplicate(client):
    payload = {"agent_name": "Jasper.ai"}

    # First save should succeed
    response1 = client.post("/api/highlights/Jasper.ai", json=payload)
    assert response1.status_code == 201

    # Second save with same agent_name should fail
    response2 = client.post("/api/highlights/Jasper.ai", json=payload)
    assert response2.status_code == 400
    assert response2.json()["detail"] == "Highlight already exists"


def test_list_highlights(client, test_session):
    # Insert a highlight directly for the test user
    highlight = Highlight(user_id=TEST_USER_ID, agent_name="Jasper.ai")
    test_session.add(highlight)
    test_session.commit()

    response = client.get("/api/highlights")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert any(h["agent_name"] == "Jasper.ai" for h in data["items"])


def test_list_highlights_not_found(client):
    # No highlights inserted, should raise 404
    response = client.get("/api/highlights")
    assert response.status_code == 404
    assert response.json()["detail"] == "No highlighted AI agents found for this user"


def test_delete_highlight(client, test_session):
    # Insert highlight to delete
    highlight = Highlight(user_id=TEST_USER_ID, agent_name="Jasper.ai")
    test_session.add(highlight)
    test_session.commit()

    highlight_id = highlight.id
    response = client.delete(f"/api/highlights/{highlight_id}")
    assert response.status_code == 204

    # Confirm deletion
    deleted = test_session.query(Highlight).filter(Highlight.id == highlight_id).first()
    assert deleted is None


def test_delete_highlight_not_found(client):
    response = client.delete("/api/highlights/999999") 
    assert response.status_code == 404
    assert response.json()["detail"] == "Highlight not found"
