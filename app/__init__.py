import os

from flask import Flask
from flask_jsonrpc import JSONRPC
from flask_migrate import Migrate
from flask_basicauth import BasicAuth
from flask_sqlalchemy import SQLAlchemy
from flask_celeryext import FlaskCeleryExt

from app.celery_utils import make_celery
from app.config import config

db = SQLAlchemy()
migrate = Migrate()
ext_celery = FlaskCeleryExt(create_celery_app=make_celery)
base_auth = BasicAuth()
jsonrpc = JSONRPC()


def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get("FLASK_CONFIG", "development")

    app = Flask(__name__)

    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    # from .users import users_blueprint
    from app.products.views import products_blueprint
    from app.orders.views import orders_blueprint

    # app.register_blueprint(users_blueprint)
    app.register_blueprint(products_blueprint)
    app.register_blueprint(orders_blueprint)

    @app.route("/all_routes", methods=["GET"])
    def all_routes():
        routes = []
        for rule in app.url_map.iter_rules():
            route = {
                "endpoint": rule.endpoint,
                "methods": ",".join(rule.methods),
                "path": str(rule),
            }
            routes.append(route)
        return {"routes": routes}

    @app.shell_context_processor
    def ctx():
        return {
            "app": app,
            "db": db,
        }

    return app
