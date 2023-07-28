from flask import Blueprint

addresses_blueprint = Blueprint(
    "adresses", __name__, url_prefix="/adresses", template_folder="templates"
)

from . import models
