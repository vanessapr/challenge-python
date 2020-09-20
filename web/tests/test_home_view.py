import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app(modules=[])
    app.config['TESTING'] = True
    test_client = app.test_client()

    yield test_client


def test_home_view(client):
    response = client.get('/')
    assert response.status_code is 200
