from flask import Blueprint

orders_blueprint = Blueprint(
    "orders", __name__, url_prefix="/orders", template_folder="templates"
)

# from . import models  # noqa

try:
    from . import tasks  # noqa
except ImportError:
    pass
