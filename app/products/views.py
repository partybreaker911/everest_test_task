from typing import Union

from flask import (
    Response,
    render_template,
    request,
    redirect,
    url_for,
)

from app import db
from app.products.models import Product
from app.products.controller import (
    product_list,
    product_delete,
    product_view,
    product_create,
    product_update,
)
from app.products import products_blueprint


@products_blueprint.route("/", methods=["GET"])
def list_of_products() -> str:
    """
    Retrieve a list of products and render the template.

    Returns:
        str: The rendered HTML template.
    """
    products = product_list()

    return render_template(
        "templates/products/list_of_products.html", products=products
    )


@products_blueprint.route("/<int:product_id>", methods=["GET"])
def show_product(product_id: int) -> str:
    """Render the template for displaying a product.

    Args:
        product_id (int): The ID of the product.

    Returns:
        str: The rendered HTML template.
    """
    product = product_view(product_id)

    return render_template("templates/products/show_product.html", product=product)


@products_blueprint.route("/products/new", methods=["GET", "POST"])
def create_product() -> None:
    """
    Create a new product.

    Args:
        None.

    Returns:
        None.
    """
    if request.method == "POST":
        name = request.form["name"]
        price = float(request.form["price"])
        color = request.form["color"]
        weight = float(request.form["weight"])
        description = request.form["description"]

        new_product = product_create(name, price, color, weight, description)
        return redirect(url_for("list_products"))

    return render_template(
        "templates/products/product_form.html", title="Create Product"
    )


@products_blueprint.route("/products/<int:id>/edit", methods=["GET", "POST"])
def edit_product(id: int) -> Union[Response, str]:
    """
    Edit a product.

    Args:
        id (int): The ID of the product to be edited.

    Returns:
        Union[Response, str]: A redirect response to view the edited product or a rendered template for the product form.
    """

    product = product_view(id)

    if request.method == "POST":
        name = request.form["name"]
        price = float(request.form["price"])
        color = request.form["color"]
        weight = float(request.form["weight"])
        description = request.form["description"]

        product = product_update(id, name, price, color, weight, description)
        return redirect(url_for("view_product", id=id))

    return render_template(
        "templates/products/product_form.html", title="Edit Product", product=product
    )


@products_blueprint.route("/products/<int:id>/delete", methods=["POST"])
def delete_product(id: int) -> redirect:
    """
    Delete a product by its ID.

    :param id: The ID of the product to delete.
    :type id: int
    :return: A redirect response to the list_products route.
    :rtype: redirect
    """
    product_delete(id)

    return redirect(url_for("list_products"))
