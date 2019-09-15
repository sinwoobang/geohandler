from typing import Type

from flask import Flask

from config import Config


def create_app(config: Type[Config]) -> Flask:
    """Create an Flask app."""
    app = Flask(__name__)

    # Add Blueprints
    from geohandler.apis.health import api_health_bp
    from geohandler.apis.meta.assets import api_meta_assets_bp
    app.register_blueprint(api_health_bp)
    app.register_blueprint(api_meta_assets_bp)

    app.config.from_object(config)
    return app
