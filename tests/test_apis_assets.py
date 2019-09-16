import http
from typing import Dict, Union

import geojson
import pytest
from flask.testing import FlaskClient
from geojson import Point

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


def test_assets(client: FlaskClient):
    """Test for /api/meta/assets"""
    url = '/api/meta/assets'
    lat = 35.818329
    lon = 128.251586
    radius = 100
    building = 'building1'
    asset_tracking_ids = ['1']

    params_type = Dict[str, Union[str, float]]

    # Without any params
    res = client.get(url)
    assert res.json['code'] == http.HTTPStatus.BAD_REQUEST

    # Without building.
    params: params_type = {
        'lat': lat,
        'lon': lon,
        'radius': radius
    }
    res = client.get(url, query_string=params)
    assert res.json['code'] == http.HTTPStatus.BAD_REQUEST

    # Without asset tracking ids.
    params: params_type = {  # type: ignore
        'lat': lat,
        'lon': lon,
        'radius': radius,
        'building': building
    }

    res = client.get(url, query_string=params)
    assert res.json['code'] == http.HTTPStatus.BAD_REQUEST

    # With everything
    params = {
        'lat': lat,
        'lon': lon,
        'radius': radius,
        'building': building,
        'assetTrackingIds': ','.join(asset_tracking_ids)
    }
    res = client.get(url, query_string=params)
    res_json = res.json
    assert res_json['code'] == http.HTTPStatus.OK  # type: ignore

    res_raw_data = res_json['data']  # geojson
    print(res_raw_data)
    res_data = geojson.loads(res_raw_data)
    res_data_feature = res_data['features'][0]
    res_data_properties = res_data_feature['properties']
    assert res_data_feature['id'] == '1'
    assert res_data_feature['geometry'] == Point((lon, lat))
    assert res_data_properties['assetTrackingId'] == asset_tracking_ids[0]
    assert res_data_properties['buildingRef'] == building
    assert res_data_properties['radius'] == radius


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
