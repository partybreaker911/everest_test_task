from flask_admin.contrib.sqla import ModelView


class ProductAdmin(ModelView):
    column_list = ("id", "name", "price", "color", "weigth")


class CategoryAdmin(ModelView):
    column_list = ("id", "name")


class CategoryProductAdmin(ModelView):
    column_list = ["id", "product", "category"]
