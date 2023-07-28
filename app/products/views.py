from typing import Union

from flask import Blueprint
from flask import (
    Response,
    render_template,
    request,
    redirect,
    url_for,
)

from . import products_blueprint
from app.products.controller import (
    product_list,
    product_delete,
    product_view,
    product_create,
    product_update,
)
from app.products.forms import ProductForm


@products_blueprint.route("/", methods=["GET"])
def list_of_products() -> str:
    """
    Retrieve a list of products and render the template.

    Returns:
        str: The rendered HTML template.
    """
    products = product_list()

    return render_template("products/list_of_products.html", products=products)


@products_blueprint.route("/<int:id>", methods=["GET"])
def show_product(id: int) -> str:
    """Render the template for displaying a product.

    Args:
        product_id (int): The ID of the product.

    Returns:
        str: The rendered HTML template.
    """
    product = product_view(id)

    return render_template("products/show_product.html", product=product)


@products_blueprint.route("/products/new", methods=["GET", "POST"])
def create_product() -> None:
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


@products_blueprint.route("/products/<int:id>/edit", methods=["GET", "POST"])
def edit_product(id: int) -> Union[Response, str]:
    product = product_view(id)
    form = ProductForm(obj=product)

    if form.validate_on_submit():
        # Extract form data
        name = form.name.data
        price = form.price.data
        color = form.color.data
        weight = form.weight.data
        description = form.description.data

        product_update(id, name, price, color, weight, description)
        return redirect(url_for("view_product", id=id))

    return render_template(
        "products/product_form.html", title="Edit Product", form=form
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

    return redirect(url_for("products.list_of_products"))
