from flask_admin.contrib.sqla import ModelView

from app import db, admin

from app.orders.models import Order


# Create the Order model admin view
class OrderAdmin(ModelView):
    # Customize the Order admin view if needed
    column_list = ["id", "quantity", "delivery_status", "created_at"]
    # ...


# # Register the Order model view with the admin
admin.add_view(OrderAdmin(Order, db.session))
