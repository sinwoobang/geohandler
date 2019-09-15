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


def test_index(client: FlaskClient):
    """Test for /api/meta/assets"""
    url = '/api/meta/assets'
    res = client.get(url)
    assert res.json['code'] == http.HTTPStatus.OK


def test_assets_id(client: FlaskClient):
    """Test for /api/meta/assets/<id>"""
    url = '/api/meta/assets/1'
    res = client.get(url)
    assert res.json['code'] == http.HTTPStatus.OK

    res = client.post(url)
    assert res.json['code'] == http.HTTPStatus.METHOD_NOT_ALLOWED  # Method Not Allowed

    res = client.put(url)
    assert res.json['code'] == http.HTTPStatus.OK

    res = client.patch(url)
    assert res.json['code'] == http.HTTPStatus.OK
