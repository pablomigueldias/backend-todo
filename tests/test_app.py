from http import HTTPStatus

from backend_todo.schemas import UsersPublic


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
    assert response.json() == {'users': []}


def test_list_user_with_users(client, user):
    user_schema = UsersPublic.model_validate(user).model_dump()
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_update_users(client, user):
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


def test_delete_user(client, user):
    response = client.delete('/users/1')

    expected_response = {'message': 'User deleted'}

    assert response.json() == expected_response
    assert response.status_code == HTTPStatus.OK


def teste_delete_user_not_found(client):
    response = client.delete('/users/0')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json().get('detail') == 'User not found'


def test_update_integrity_erro(client, user):
    client.post(
        '/users',
        json={
            'username': 'fausto',
            'email': 'fausto@exemple.com',
            'password': 'secret',
        },
    )
    response = client.put(
        f'/users/{user.id}',
        json={
            'username': 'fausto',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Username or Email already exists'}
