from flask import Blueprint

customers_blueprint = Blueprint(
    "customers", __name__, url_prefix="/customers", template_folder="templates"
)


from . import models
