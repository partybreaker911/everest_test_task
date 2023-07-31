from flask import Blueprint

address_blueprint = Blueprint(
    "address", __name__, url_prefix="/address", template_folder="templates"
)

from . import models
