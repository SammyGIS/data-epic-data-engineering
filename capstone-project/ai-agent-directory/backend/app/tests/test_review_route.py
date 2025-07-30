import os
import sys
import uuid
from datetime import datetime

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Path adjustment
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

os.environ["DATABASE_URL"] = "sqlite://"
os.environ["TESTING"] = "true"

from api.route.review import review_router
from auth.dependency import get_current_user
from core.database import Base, get_db
from core.models.user import User
from core.models.review import Review
from core.models.agent import Agent

# DB setup
TEST_SQLALCHEMY_DATABASE_URL = "sqlite://"
test_engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


@pytest.fixture(scope="function")
def test_session():
    connection = test_engine.connect()
    transaction = connection.begin()
    Base.metadata.create_all(bind=connection)

    session = TestingSessionLocal(bind=connection)

    try:
        user_id = uuid.UUID("12345678-1234-5678-1234-567812345678")
        user = User(
            id=user_id,
            first_name="John",
            last_name="Doe",
            username="johndoe",
            email="john@example.com",
            hashed_password="hashed",
        )
        session.add(user)

        agent = Agent(name="AgentSmith", description="Test agent", homepage_url="example.com", category="TestCorp")
        session.add(agent)

        session.commit()
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()
        Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(scope="function")
def client(test_session):
    app = FastAPI()
    app.include_router(review_router)

    def override_get_db():
        yield test_session

    def mock_user():
        return User(
            id=uuid.UUID("12345678-1234-5678-1234-567812345678"),
            username="johndoe",
            email="john@example.com",
            is_admin=False,
        )

    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_current_user] = mock_user

    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()


def test_create_review(client):
    payload = {
        "rating": 4,
        "comment": "Very good service"
    }
    response = client.post("/agents/AgentSmith/review", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["rating"] == 4
    assert data["comment"] == "Very good service"
    assert data["agent_name"] == "AgentSmith"


def test_create_duplicate_review(client):
    payload = {
        "rating": 5,
        "comment": "Excellent!"
    }
    # First review
    client.post("/agents/AgentSmith/review", json=payload)
    # Second review (should fail)
    response = client.post("/agents/AgentSmith/review", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Review already exists for this agent by this user"


def test_get_reviews_success(client):
    # Create a review
    payload = {"rating": 5, "comment": "Great!"}
    client.post("/agents/AgentSmith/review", json=payload)

    # Get reviews
    response = client.get("/agents/AgentSmith/reviews")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 1
    assert data["items"][0]["agent_name"] == "AgentSmith"


def test_get_reviews_not_found(client):
    response = client.get("/agents/UnknownAgent/reviews")
    assert response.status_code == 404
    assert response.json()["detail"] == "No reviews found for this agent"
