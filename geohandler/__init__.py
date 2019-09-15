import http
from typing import Type

from flask import Flask

from config import Config


def create_app(config: Type[Config]) -> Flask:
    """Create an Flask app."""
    app = Flask(__name__)

    # Setup config
    app.config.from_object(config)

    # Add Blueprints
    from geohandler.apis.health import api_health_bp
    from geohandler.apis.meta.assets import api_meta_assets_bp
    app.register_blueprint(api_health_bp)
    app.register_blueprint(api_meta_assets_bp)

    if app.testing or app.debug:  # Blueprints which are used only for test/debug
        from geohandler.apis.error_handler import api_error_bp
        app.register_blueprint(api_error_bp)

    # Add error handlers
    from geohandler.apis.error_handler import (
        handle_not_found, handle_method_not_allowed,
        handle_internal_server_error
    )
    app.register_error_handler(http.HTTPStatus.NOT_FOUND, handle_not_found)
    app.register_error_handler(http.HTTPStatus.METHOD_NOT_ALLOWED, handle_method_not_allowed)
    app.register_error_handler(http.HTTPStatus.INTERNAL_SERVER_ERROR, handle_internal_server_error)
    return app
