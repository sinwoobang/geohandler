import http
import geojson

from typing import List, Optional
from flask import Blueprint, request
from flask.views import MethodView
from geojson import FeatureCollection, Feature, Point

# Didn't use the prefix '/api/meta/assets' but '/api/meta' because some api use 'asset' not 'assets'.
api_meta_assets_bp = Blueprint('api_meta_assets_bp', __name__, url_prefix='/api/meta')


class MetaAssetsAPI(MethodView):
    def get(self):
        raw_sources = request.args.get('sources', '', str)
        sources: List[str] = raw_sources.split(',')

        lat: Optional[float] = request.args.get('lat', type=float)
        lon: Optional[float] = request.args.get('lon', type=float)
        radius: Optional[float] = request.args.get('radius', type=float)
        if not lat or not lon or not radius:
            return {
                'code': http.HTTPStatus.BAD_REQUEST,
                'message': http.HTTPStatus.BAD_REQUEST.phrase,
                'error': 'Data lat, lon, radius are required.'
            }

        raw_bbox = request.args.get('bbox', '', str)
        try:
            bbox: List[float] = list(map(float, raw_sources.split(',')))
        except (TypeError, ValueError):  # Case of None
            bbox = []

        building: Optional[str] = request.args.get('building', type=str)
        if not building:
            return {
                'code': http.HTTPStatus.BAD_REQUEST,
                'message': http.HTTPStatus.BAD_REQUEST.phrase,
                'error': 'Data building is required.'
            }

        raw_asset_tracking_ids = request.args.get('assetTrackingIds', '', str)
        asset_tracking_ids: List[str] = raw_asset_tracking_ids.split(',')
        if not asset_tracking_ids[0]:  # the value of [0] will be empty string if there is nothing.
            return {
                'code': http.HTTPStatus.BAD_REQUEST,
                'message': http.HTTPStatus.BAD_REQUEST.phrase,
                'error': 'Data assetTrackingIds is required.'
            }

        raw_tags_any = request.args.get('tags_any', '', str)
        tags_any: List[str] = raw_asset_tracking_ids.split(',')

        raw_tags_all = request.args.get('tags_all', '', str)
        tags_all: List[str] = raw_asset_tracking_ids.split(',')

        operator: Optional[str] = request.args.get('operator', type=str)
        advertiser: Optional[str] = request.args.get('advertiser', type=str)
        limit: Optional[int] = request.args.get('limit', type=int)

        point = Point((lon, lat))
        properties = {
            'radius': radius,
            'assetTrackingId': asset_tracking_ids[0],
            'buildingRef': building
        }
        feature = Feature(id="1", geometry=point, properties=properties)
        features = [feature]
        feature_collection = FeatureCollection(features=features)
        return {
            'code': http.HTTPStatus.OK,
            'message': http.HTTPStatus.OK.phrase,
            'data': geojson.dumps(feature_collection)
        }

    def post(self):
        return {'code': http.HTTPStatus.OK, 'message': 'This is POST.'}

    def delete(self):
        return {'code': http.HTTPStatus.OK, 'message': 'This is DELETE.'}


class MetaAssetsIDAPI(MethodView):
    def get(self, id):
        return {'code': http.HTTPStatus.OK, 'message': 'This is GET.'}

    def delete(self, id):
        return {'code': http.HTTPStatus.OK, 'message': 'This is DELETE.'}

    def patch(self, id):
        return {'code': http.HTTPStatus.OK, 'message': 'This is PATCH.'}

    def put(self, id):
        return {'code': http.HTTPStatus.OK, 'message': 'This is PUT.'}


class MetaAssetUploadAPI(MethodView):
    def post(self):
        return {'code': http.HTTPStatus.OK, 'message': 'This is POST.'}


class MetaAssetsMergeAPI(MethodView):
    def post(self):
        return {'code': http.HTTPStatus.OK, 'message': 'This is POST.'}


class MetaAssetsResetAPI(MethodView):
    def post(self):
        return {'code': http.HTTPStatus.OK, 'message': 'This is POST.'}


api_meta_assets_bp.add_url_rule('/assets', view_func=MetaAssetsAPI.as_view('meta_assets_api'))
api_meta_assets_bp.add_url_rule('/assets/<id>', view_func=MetaAssetsIDAPI.as_view('meta_assets_id_api'))
api_meta_assets_bp.add_url_rule('/assetUpload', view_func=MetaAssetUploadAPI.as_view('meta_asset_upload_api'))
api_meta_assets_bp.add_url_rule('/assets/merge', view_func=MetaAssetsMergeAPI.as_view('meta_assets_merge_api'))
api_meta_assets_bp.add_url_rule('/assets/reset', view_func=MetaAssetsResetAPI.as_view('meta_assets_reset_api'))
