from flask import Blueprint

catalog_blueprint = Blueprint("catalog", __name__, template_folder="templates")

from . import models, views
