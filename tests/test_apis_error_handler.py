import http

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


def test_error_handlers(client: FlaskClient):
    """Test error handlers"""
    url = '/api/error/notfound'
    res = client.get(url)
    assert res.json['code'] == http.HTTPStatus.NOT_FOUND

    url = '/api/error/methodnotallowed'
    res = client.get(url)
    assert res.json['code'] == http.HTTPStatus.METHOD_NOT_ALLOWED

    url = '/api/error/internalservererror'
    res = client.get(url)
    assert res.json['code'] == http.HTTPStatus.INTERNAL_SERVER_ERROR
