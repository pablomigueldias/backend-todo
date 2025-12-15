from http import HTTPStatus

from fastapi.testclient import TestClient

from backend_todo.app import app


def test_root_deve_retornar_ola_mundo():
    client = TestClient(app)
    response = client.get('/')

    assert response.json() == {'message': 'Hello, World!'}
    assert response.status_code == HTTPStatus.OK


def test_user():
    client = TestClient(app)
    response = client.post(
        '/users',
        json={
            'username': 'pablo',
            'password': 'testpass',
            'email': 'pablo@exemple.com',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'pablo',
        'email': 'pablo@exemple.com',
    }
