import pytest
from httpx import AsyncClient
from fastapi import status
from src.main import app


def test_read_root(client):
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello World!"}