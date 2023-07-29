from flask_admin.contrib.sqla import ModelView


class ProductAdmin(ModelView):
    """ModelView for product admin."""

    can_view_details = True
    column_display_pk = True
    column_list = [
        "id",
        "categories",
        "name",
        "price",
        "color",
        "weight",
        "description",
    ]
    please_do_show_prorimary_keys_value = True


class CategoryAdmin(ModelView):
    """ModelView for category admin."""

    can_view_details = True
    column_display_pk = True
    column_list = [
        "id",
        "name",
        "parent",
    ]
    please_do_show_prorimary_keys_value = True
