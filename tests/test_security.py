from http import HTTPStatus

from jwt import decode

from backend_todo.security import ALGORITHM, SECRET_KEY, create_access_token


def test_create_access_token():
    data = {'test': 'testuser'}
    token = create_access_token(data)
    decoded = decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    # Valide a chave correta
    assert decoded['test'] == data['test']
    assert 'exp' in decoded


def test_jwt_decode_invalid_token(client):
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer invalidtoken'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
