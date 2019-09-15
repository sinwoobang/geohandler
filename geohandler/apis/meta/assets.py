import http

from flask import Blueprint
from flask.views import MethodView


# Didn't use the prefix '/api/meta/assets' but '/api/meta' because some api use 'asset' not 'assets'.
api_meta_assets_bp = Blueprint('api_meta_assets_bp', __name__, url_prefix='/api/meta')


class MetaAssetsAPI(MethodView):
    def get(self):
        return {'code': http.HTTPStatus.OK, 'message': 'This is GET.'}

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
