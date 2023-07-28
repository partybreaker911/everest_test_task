from flask_admin.contrib.sqla import ModelView
from app.products.models import Product
from app import admin, db


class ProductAdmin(ModelView):
    column_list = ["id", "name", "price", "color", "weight", "description"]


admin.add_view(ProductAdmin(Product, db.session))
