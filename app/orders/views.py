from typing import Union

from flask import Blueprint
from flask import (
    Response,
    render_template,
    request,
    redirect,
    url_for,
)

from app.orders.controller import (
    create_order,
    order_update,
    order_list,
    get_order_by_id,
    order_delete,
)
from app.orders.forms import OrderForm, OrderUpdateForm
from app.products.models import Product
from app.orders import orders_blueprint
from app.products.controller import product_list


@orders_blueprint.route("/", methods=["GET"])
def orders_list() -> str:
    """
    View function for displaying a list of orders.

    Returns:
        str: The rendered HTML template of the list of orders.
    """
    orders = order_list()
    return render_template("orders/list_of_orders.html", orders=orders)


@orders_blueprint.route("/<int:order_id>", methods=["GET"])
def order_view(order_id: int) -> str:
    """
    View function for displaying a single order.

    Args:
        order_id (int): The ID of the order.

    Returns:
        str: The rendered HTML template of the order.
    """
    order = get_order_by_id(order_id)
    return render_template("orders/show_order.html", order=order)


@orders_blueprint.route("/create", methods=["GET", "POST"])
def order_create() -> None:
    form = OrderForm()

    if form.validate_on_submit():
        # Extract form data
        quantity = form.quantity.data
        product_id = form.product_id.data
        status = form.status.data

        # Call the controller function to create the order
        create_order(quantity, product_id, status)

        # Redirect to the product list page or any other appropriate page
        return redirect(url_for("products.list_of_products"))

    return render_template("orders/order_create.html", form=form)


@orders_blueprint.route("/<int:order_id>/update", methods=["GET", "POST"])
def order_update(order_id: int) -> Union[str, Response]:
    order = get_order_by_id(order_id)
    # print(order.id)
    form = OrderForm(obj=order)

    if form.validate_on_submit():
        # Get the submitted form data
        quantity = form.quantity.data
        product_id = form.product_id.data
        status = form.status.data

        if order_update(
            order_id=order_id, quantity=quantity, product_id=product_id, status=status
        ):
            return redirect(url_for("orders.list_orders"))
        else:
            return "Error updating order", 500

    return render_template("orders/update_order.html", form=form, order=order)


@orders_blueprint.route("/<int:order_id>/delete", methods=["POST"])
def order_delete(order_id: int) -> None:
    """
    View function for deleting an existing order.

    Args:
        order_id (int): The ID of the order.

    Returns:
        None.
    """
    order_delete(order_id)
