from flask_admin.contrib.sqla import ModelView


class CustomerAdmin(ModelView):
    """ModelView for customer admin."""

    can_view_details = True
    column_display_pk = True
    column_list = (
        "name",
        "date_of_birth",
        "email",
    )


class CustomerShippingAddressAdmin(ModelView):
    """ModelView for customer shipping address admin."""

    can_view_details = True
    column_display_pk = True
    column_list = (
        "first_name",
        "last_name",
        "country",
        "city",
        "street",
        "house_number",
        "apartment_number",
    )
