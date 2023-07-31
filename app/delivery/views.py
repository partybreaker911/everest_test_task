from flask import redirect, url_for, render_template, request, jsonify

import app

from app.delivery.controller import (
    create_order,
    get_all_order,
    update_order,
    get_order_by_id,
)
from app.delivery import delivery_blueprint
from app.delivery.forms import OrderForm
from app.delivery.models import Order
from app.catalog.models import Product


@delivery_blueprint.route("/create", methods=["GET", "POST"])
def create_order_view():
    form = OrderForm()
    form.product.choices = [
        (product.id, product.name) for product in Product.query.all()
    ]

    if form.validate_on_submit():
        order_id = create_order(form)
        return redirect(url_for("delivery.list_of_all_orders", order_id=order_id))

    return render_template("order/order_form.html", form=form)


@delivery_blueprint.route("/", methods=["GET"])
def list_of_all_orders():
    orders = get_all_order()
    return render_template("order/list_of_orders.html", orders=orders)


@delivery_blueprint.route("/edit/<int:order_id>", methods=["GET", "POST"])
def edit_order_view(order_id):
    order = Order.query.get_or_404(order_id)
    form = OrderForm(obj=order)

    if form.validate_on_submit():
        update_order(order_id, form)
        return redirect(url_for("delivery.list_of_all_orders"))

    return render_template("order/edit_order_form.html", form=form, order_id=order_id)


@delivery_blueprint.route("/jsonrpc", methods=["POST"])
def json_rpc_endpoint():
    data = request.get_json()

    if "method" not in data or "id" not in data:
        return (
            jsonify(
                {
                    "jsonrpc": "2.0",
                    "error": {"code": -32600, "message": "Invalid Request"},
                    "id": None,
                }
            ),
            400,
        )

    method_name = data["method"]
    params = data.get("params", {})

    if method_name == "order.get_status":
        order_id = params.get("order_id")
        if order_id is None:
            return (
                jsonify(
                    {
                        "jsonrpc": "2.0",
                        "error": {"code": -32602, "message": "Invalid params"},
                        "id": data["id"],
                    }
                ),
                400,
            )

        try:
            order = Order.query.get(order_id)
            if order:
                return (
                    jsonify(
                        {
                            "jsonrpc": "2.0",
                            "result": {"status": order.status.value},
                            "id": data["id"],
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "jsonrpc": "2.0",
                            "error": {"code": -32000, "message": "Order not found"},
                            "id": data["id"],
                        }
                    ),
                    404,
                )
        except Exception as e:
            return (
                jsonify(
                    {
                        "jsonrpc": "2.0",
                        "error": {"code": -32000, "message": str(e)},
                        "id": data["id"],
                    }
                ),
                500,
            )

    else:
        return (
            jsonify(
                {
                    "jsonrpc": "2.0",
                    "error": {"code": -32601, "message": "Method not found"},
                    "id": data["id"],
                }
            ),
            404,
        )
