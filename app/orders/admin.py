from flask_admin.contrib.sqla import ModelView

from app import db, admin

# from app.orders.tasks import change_order_status
from app.orders.models import Order, OrderAddress


# Create the Order model admin view
class OrderAdmin(ModelView):
    # Customize the Order admin view if needed
    column_list = ["id", "product", "quantity", "status", "created_at"]
    column_filters = ["id", "status", "created_at"]
    column_searchable_list = ["status"]
    # def on_model_change(self, form, model, is_created):
    #     if not is_created and "status" in form.changed_data:
    #         # Get the new status value from the form data
    #         new_status_value = form.status.data

    #         # Call the Celery task to update the status asynchronously
    #         change_order_status.delay(model.id, new_status_value)


class OrderAddressAdmin(ModelView):
    column_list = ["id", "order_id", "country_id", "city_id", "street_id"]


# # Register the Order model view with the admin
admin.add_view(OrderAdmin(Order, db.session))
admin.add_view(OrderAddressAdmin(OrderAddress, db.session))
