import os

from flask import Flask
from flask_celeryext import FlaskCeleryExt
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_admin import Admin
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from flask_security.models import fsqla_v3 as fsqla
from flask_mail import Mail
from app.celery_utils import make_celery
from app.config import config


# instantiate the extensions
db = SQLAlchemy()
migrate = Migrate()
ext_celery = FlaskCeleryExt(create_celery_app=make_celery)
csrf = CSRFProtect()
socketio = SocketIO()
# login_manager = LoginManager()
admin = Admin(name="Catalog", template_mode="bootstrap4")
security = Security()
mail = Mail()


def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get("FLASK_CONFIG", "development")

    # instantiate the app
    app = Flask(__name__)

    # set config
    app.config.from_object(config[config_name])

    # set up extensions
    db.init_app(app)
    fsqla.FsModels.set_db_info(db)
    from app.users.models import User, Role

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security = Security(app, user_datastore)
    migrate.init_app(app, db)
    ext_celery.init_app(app)
    # csrf.init_app(app)
    mail.init_app(app)
    socketio.init_app(app, message_queue=app.config["SOCKETIO_MESSAGE_QUEUE"])

    admin.init_app(app)
    # login_manager.init_app(app)

    # from app.users.models import load_user

    # login_manager.user_loader(load_user)
    from app.users import users_blueprint
    from app.catalog import catalog_blueprint
    from app.delivery import delivery_blueprint
    from app.addresses import address_blueprint

    app.register_blueprint(address_blueprint)
    app.register_blueprint(delivery_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(catalog_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
