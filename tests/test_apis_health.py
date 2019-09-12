import pytest
from flask.testing import FlaskClient

from config import TestingConfig
from geohandler import create_app


@pytest.fixture
def client():
    """Setup Test environment for Flask"""
    app = create_app(TestingConfig)

    client = app.test_client()

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    yield client  # this is where the testing happens!

    ctx.pop()


def test_index(client: FlaskClient):
    """Test for /api/health/"""
    url = '/api/health/'
    res = client.get(url)
    assert res.data == b'ok'
