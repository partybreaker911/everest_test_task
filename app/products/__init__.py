from flask import Blueprint

products_blueprint = Blueprint(
    "products", __name__, url_prefix="/products", template_folder="templates"
)

from . import models  # noqa

try:
    from . import tasks  # noqa
except ImportError:
    pass
