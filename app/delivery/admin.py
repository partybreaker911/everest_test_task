from flask_admin.contrib.sqla import ModelView


class OrderAdmin(ModelView):
    column_list = ("id", "status", "created_at")


class OrderDetailAdmin(ModelView):
    column_list = ["id", "product_id", "order_id"]


class OrderAddressAdmin(ModelView):
    column_list = [
        "id",
        "address",
        "country",
        "city",
        "street",
    ]
