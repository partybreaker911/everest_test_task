from flask import Blueprint

delivery_blueprint = Blueprint(
    "delivery", __name__, url_prefix="/delivery", template_folder="templates"
)


from . import models, views, admin
