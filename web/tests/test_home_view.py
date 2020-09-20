import pytest
from injector import Binder
from unittest.mock import MagicMock
from use_cases.i_list_use_case import IListUseCase
from use_cases.list_use_case import ListUseCase
from use_cases.exceptions import InvalidEntryList
from app import create_app


def configure_bindings(binder: Binder) -> Binder:
    binder.bind(IListUseCase, ListUseCase)


@pytest.fixture
def client():
    app = create_app(modules=[configure_bindings])
    app.config['TESTING'] = True
    app.secret_key = 'some_secret'
    test_client = app.test_client()

    yield test_client


def test_home_view(client):
    response = client.get('/')
    assert response.status_code is 200


def test_home_view_get_include_input_field(client):
    response = client.get('/')
    assert b'input' in response.data
    assert b'submit' in response.data


def test_home_view_post_invalid_input(client):
    list_use_case: IListUseCase = MagicMock(IListUseCase)
    list_use_case.flatten_list.side_effect = InvalidEntryList
    response = client.post('/', data={'input': '1, 2, 3, 4'})
    assert response.status_code == 400
    assert bytes('Invalid input list. Please try again!', 'utf-8') in response.data


def test_home_view_post_valid_output(client):
    list_use_case: IListUseCase = MagicMock(IListUseCase)
    list_use_case.flatten_list.return_value = [1, 2, 3, 4, 5, 6, 7, 8]
    response = client.post('/', data={'input': '[1, 2, [3, 4, [5, 6], 7], 8]'})
    assert response.status_code == 200
    assert b'[1, 2, 3, 4, 5, 6, 7, 8]' in response.data
