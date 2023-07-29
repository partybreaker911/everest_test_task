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
from app.orders.forms import OrderForm
from app.orders import orders_blueprint


@orders_blueprint.route("/", methods=["GET"])
def orders_list() -> Union[str, Response]:
    """
    View function for displaying a list of orders.

    Args:
        None

    Returns:
        Union[str, Response]: The rendered HTML template of the list of orders.
    """
    orders = order_list()
    return render_template("orders/list_of_orders.html", orders=orders)


@orders_blueprint.route("/<int:order_id>", methods=["GET"])
def order_view(order_id: int) -> Union[str, Response]:
    """Display a single order.

    Args:
        order_id (int): The ID of the order.

    Returns:
        Union[str, Response]: The rendered HTML template of the order.
    """
    order = get_order_by_id(order_id)
    return render_template("orders/show_order.html", order=order)


@orders_blueprint.route("/create", methods=["GET", "POST"])
def order_create() -> Union[str, Response]:
    """
    Create a new order.

    Handles the "/create" endpoint of the orders blueprint.
    Accepts both GET and POST requests.

    Returns:
    - Union[str, Response]: The result of the function, either a string or a Flask Response object.

    Side Effects:
    - Extracts form data from the OrderForm object.
    - Calls the controller function create_order with the extracted form data.
    - Redirects to the product list page or any other appropriate page if the form is valid.
    - Renders the "orders/order_create.html" template with the OrderForm object if the form is invalid.
    """
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
    """
    Updates an order with the specified order ID.

    Parameters:
        order_id (int): The ID of the order to be updated.

    Returns:
        Union[str, Response]: If the order update is successful, it redirects to the list_orders page. Otherwise, it returns an error message with status code 500.
    """
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
def order_delete(order_id: int) -> Union[str, Response]:
    """
    Delete an existing order.

    Args:
        order_id (int): The ID of the order to be deleted.

    Returns:
        Union[str, Response]: A string or a Flask Response object.
    """
    order_delete(order_id)
