from flask import Blueprint
from flask import (
    Response,
    render_template,
    request,
    redirect,
    url_for,
)

from app.orders.controller import (
    order_create,
    order_update,
    order_list,
    order_view,
    order_delete,
)
from app.orders.forms import OrderForm
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
    order = order_view(order_id)
    return render_template("orders/show_order.html", order=order)


@orders_blueprint.route("/create", methods=["GET", "POST"])
def order_create() -> None:
    form = OrderForm()
    form.product_id.choices = [(product.id, product.name) for product in product_list()]

    if form.validate_on_submit():
        quantity = form.quantity.data
        product_id = form.product_id.data

        try:
            order = order_create(quantity=quantity, product_id=product_id)
        except ValueError as e:
            return str(e), 404

        return redirect(url_for("products.list_products"))

    return render_template("orders/create_order.html", form=form)


@orders_blueprint.route("/<int:order_id>/update", methods=["GET", "POST"])
def order_update(order_id: int) -> None:
    """
    View function for updating an existing order.

    Args:
        order_id (int): The ID of the order.

    Returns:
        None.
    """
    return order_update(order_id)


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
