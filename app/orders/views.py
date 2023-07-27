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


orders_blueprint = Blueprint(
    "orders", __name__, url_prefix="/orders", template_folder="templates"
)


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


@orders_blueprint.route("/new", methods=["GET", "POST"])
def order_create() -> None:
    """
    Create a new order.

    Returns:
        redirect: Redirect to the product list page after creating the order.
    """
    if request.method == "POST":
        try:
            quantity = int(request.form["quantity"])
            product_id = int(request.form["product_id"])
        except ValueError:
            return "Invalid input", 400

        try:
            # Create the order using the controller function
            order = order_create(quantity=quantity, product_id=product_id)
        except ValueError as e:
            return str(e), 404

        # You can perform any additional actions or error handling here if needed

        return redirect(
            url_for("products.list_products")
        )  # Redirect to the product list page

    # Render the HTML template for creating a new order
    return render_template("orders/create_order.html")


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
