from flask_admin.contrib.sqla import ModelView

from app.products.models import Product


# Create the Product model admin view
class ProductAdmin(ModelView):
    # Set the database session for the view
    def __init__(self, session, **kwargs):
        super(ProductAdmin, self).__init__(Product, session, **kwargs)

    # Customize the columns to display in the list view
    column_list = ["id", "name", "price", "color", "weight", "description"]

    # Add filters to the list view
    column_filters = ["name", "price", "color"]

    # Enable search box for the list view
    column_searchable_list = ["name", "description"]

    # Set column labels
    column_labels = {
        "id": "ID",
        "name": "Product Name",
        "price": "Product Price",
        "color": "Product Color",
        "weight": "Product Weight",
        "description": "Description",
    }

    # Set form fields to display when creating or editing a product
    form_columns = ["name", "price", "color", "weight", "description"]

    # Customize the form field labels
    form_args = {
        "name": {"label": "Product Name"},
        "price": {"label": "Product Price"},
        "color": {"label": "Product Color"},
        "weight": {"label": "Product Weight"},
        "description": {"label": "Description"},
    }

    # Enable CSRF protection for the forms
    form_excluded_columns = ["orders"]

    # Allow ordering by columns in the list view
    column_default_sort = ("id", True)

    # Set the page size for the list view
    page_size = 20
