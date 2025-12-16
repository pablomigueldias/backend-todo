from http import HTTPStatus


def test_user(client):
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


def test_list_users(client):
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{'id': 1, 'username': 'pablo', 'email': 'pablo@exemple.com'}]
    }


def test_update_users(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'pablo',
            'password': 'testpass',
            'email': 'pablo@exemple.com',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'pablo',
        'email': 'pablo@exemple.com',
    }


def test_update_users_not_found(client):
    response = client.put(
        '/users/0',
        json={
            'username': 'pablo',
            'password': 'testpass',
            'email': 'pablo@exemple.com',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')

    expected_response = {
        'id': 1,
        'username': 'pablo',
        'email': 'pablo@exemple.com',
        'password': 'testpass',
    }

    assert response.json() == expected_response
    assert response.status_code == HTTPStatus.OK


def teste_delete_user_not_found(client):
    response = client.delete('/users/0')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json().get('detail') == 'Não encontrado'
