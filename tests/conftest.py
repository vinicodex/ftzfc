import pytest
from src.main import app
from fastapi.testclient import TestClient  

@pytest.fixture
def client():
    yield TestClient(app=app)
    