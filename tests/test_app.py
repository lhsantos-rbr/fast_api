from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

import pytest

@pytest.fixture
def client():
    return TestClient(app)


def test_root_deve_retornar_ok_e_ola_mundo(client):

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_criar_usuario_deve_retornar_usuario_criado(client):

    response = client.post(
        '/users/',
        json={
            'username': 'test_user',
            'password': 'test_password',
            'email': 'test@test.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {
        'id': 1,
        'username': 'test_user',
        'email': 'test@test.com',
    }  # Assert
