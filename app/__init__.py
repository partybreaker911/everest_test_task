import os

from flask import Flask
from flask_celeryext import FlaskCeleryExt
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_admin import Admin
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

from app.celery_utils import make_celery


from app.config import config


def load_user(user_id):
    """Callback to reload the user object from the user ID stored in the session."""
    from app.users.models import User

    return User.query.get(int(user_id))


# instantiate the extensions
db = SQLAlchemy()
migrate = Migrate()
ext_celery = FlaskCeleryExt(create_celery_app=make_celery)
csrf = CSRFProtect()
socketio = SocketIO()
login_manager = LoginManager()
admin = Admin(name="Catalog", template_mode="bootstrap4")


def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get("FLASK_CONFIG", "development")

    # instantiate the app
    app = Flask(__name__)

    # set config
    app.config.from_object(config[config_name])

    # set up extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ext_celery.init_app(app)
    csrf.init_app(app)
    socketio.init_app(app, message_queue=app.config["SOCKETIO_MESSAGE_QUEUE"])

    admin.init_app(app)
    login_manager.init_app(app)
    login_manager.user_loader(load_user)

    # register blueprints
    from app.users import users_blueprint
    from app.products import products_blueprint
    from app.orders import orders_blueprint
    from app.customers import customers_blueprint

    app.register_blueprint(products_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(orders_blueprint)
    app.register_blueprint(customers_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
