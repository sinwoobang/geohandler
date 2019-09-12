from flask import Blueprint, make_response

api_health_bp = Blueprint('api_health_bp', __name__, url_prefix='/api/health')


@api_health_bp.route('/')
def index():
    """
    Health Check API
    :return:
    """
    return make_response('ok', 200)
