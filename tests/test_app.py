from http import HTTPStatus


def test_get_root(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'teste'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'isaque',
            'email': 'isaque@gmail.com',
            'password': '123',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'isaque',
        'email': 'isaque@gmail.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{'username': 'isaque', 'email': 'isaque@gmail.com', 'id': 1}]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'isaque',
            'email': 'isaque@gmail.com',
            'password': 'novasenha',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'isaque',
        'email': 'isaque@gmail.com',
        'id': 1,
    }


def test_update_user_error(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'isaque',
            'email': 'isaque@gmail.com',
            'password': 'novasenha',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_get_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'isaque',
        'email': 'isaque@gmail.com',
        'id': 1,
    }


def test_get_user_error(client):
    response = client.get('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_error(client):
    response = client.delete('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
