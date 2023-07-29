from flask import (
    render_template,
    redirect,
    url_for,
)

from app.products import products_blueprint
from app.products.forms import ProductForm
from app.products.controller import (
    get_product_by_id,
    get_all_products,
    product_create,
)


@products_blueprint.route("/", methods=["GET"])
def list_of_products() -> str:
    """
    Retrieve a list of products and render the template.

    Returns:
        str: The rendered HTML template.
    """
    products = get_all_products()

    return render_template("products/list_of_products.html", products=products)


@products_blueprint.route("/create", methods=["GET", "POST"])
def create_product() -> str:
    form = ProductForm()

    if form.validate_on_submit():
        # Extract form data
        name = form.name.data
        price = form.price.data
        color = form.color.data
        weight = form.weight.data
        description = form.description.data

        # Call the controller function to create the product
        product_create(name, price, color, weight, description)

        # Redirect to the list of products or any other appropriate page
        return redirect(url_for("products.list_of_products"))

    return render_template("products/create_product.html", form=form)


@products_blueprint.route("/<int:product_id>/view", methods=["GET"])
def view_product(product_id: int) -> str:
    """
    Retrieve a product and render the template.

    Args:
        product_id (int): The ID of the product.

    Returns:
        str: The rendered HTML template.
    """
    product = get_product_by_id(product_id)

    return render_template("products/view_product.html", product=product)
