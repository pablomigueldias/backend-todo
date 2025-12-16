import pytest
from fastapi.testclient import TestClient

from backend_todo.app import app


@pytest.fixture
def client():
    return TestClient(app)
