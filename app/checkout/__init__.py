from flask import Blueprint

checkout_blueprint = Blueprint(
    "checkout", __name__, url_prefix="/checkout", template_folder="templates"
)

from . import views
