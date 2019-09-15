import http

from flask import Blueprint, abort
from flask.views import View

# This blueprint will be added only for the test/debug environment.
api_error_bp = Blueprint('api_error_bp', __name__, url_prefix='/api/error')


class ErrorNotFoundAPI(View):
    methods = ['GET']

    def dispatch_request(self):
        raise abort(http.HTTPStatus.NOT_FOUND)


class ErrorMethodNotAllowedAPI(View):
    methods = ['GET']

    def dispatch_request(self):
        raise abort(http.HTTPStatus.METHOD_NOT_ALLOWED)


class ErrorInternalServerError(View):
    methods = ['GET']

    def dispatch_request(self):
        raise abort(http.HTTPStatus.INTERNAL_SERVER_ERROR)


api_error_bp.add_url_rule('/notfound', view_func=ErrorNotFoundAPI.as_view('api_error_not_found'))
api_error_bp.add_url_rule('/methodnotallowed', view_func=ErrorMethodNotAllowedAPI.as_view('api_error_method_not_allowed'))  # noqa
api_error_bp.add_url_rule('/internalservererror', view_func=ErrorInternalServerError.as_view('api_error_internal_server_error'))  # noqa


def handle_not_found(e):
    return {
        'code': http.HTTPStatus.NOT_FOUND,
        'error': 'not_found'
    }


def handle_method_not_allowed(e):
    return {
        'code': http.HTTPStatus.METHOD_NOT_ALLOWED,
        'error': 'method_not_allowed'
    }


def handle_internal_server_error(e):
    return {
        'code': http.HTTPStatus.INTERNAL_SERVER_ERROR,
        'error': 'internal_server_error'
    }
