from flask import (
    Response,
    render_template,
    request,
    redirect,
    url_for,
)

from app.orders import orders_blueprint
from app.orders.controller import (
    order_create,
    order_update,
    order_list,
    order_view,
    order_delete,
)


@orders_blueprint.route("/", methods=["GET"])
def orders_list() -> str:
    """
    View function for displaying a list of orders.

    Returns:
        str: The rendered HTML template of the list of orders.
    """
    orders = order_list()
    return render_template("templates/orders/list_of_orders.html", orders=orders)


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
    return render_template("templates/orders/show_order.html", order=order)


@orders_blueprint.route("/new", methods=["GET", "POST"])
def order_create() -> None:
    """
    View function for creating a new order.

    Args:
        None.

    Returns:
        None.
    """
    return order_create()


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