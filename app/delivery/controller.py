from typing import List

from app import db
from app.delivery.models import (
    Order,
    OrderDetail,
    OrderStatusEnum,
    OrderAddress,
)
from app.catalog.models import Product


def get_all_order() -> List[Order]:
    return Order.query.options(
        db.joinedload(Order.order_details), db.joinedload(Order.order_address)
    ).all()


def create_order(form):
    product_id = form.product.data
    quantity = form.quantity.data
    address = form.address.data

    order = Order(status=OrderStatusEnum.PENDING)
    db.session.add(order)

    product = Product.query.get(product_id)
    order_detail = OrderDetail(product=product, quantity=quantity)

    # Assign the order to the order_detail using the relationship name "orders"
    order_detail.orders.append(order)

    db.session.add(order_detail)

    order_address = OrderAddress(address=address)
    order_address.order = order  # Assign the order to the order_address using the relationship name "order"

    db.session.add(order_address)

    db.session.commit()

    return order.id


def update_order(order_id, form):
    order = Order.query.get(order_id)
    if not order:
        raise ValueError("Order with specified ID not found.")

    # Update the order status

    # Get the existing order_detail and update its data
    order_detail = order.order_details[0]
    product_id = form.product.data
    quantity = form.quantity.data
    product = Product.query.get(product_id)
    order_detail.product = product
    order_detail.quantity = quantity

    # Get the existing order_address and update its data
    order_address = order.order_address
    address = form.address.data
    order_address.address = address

    db.session.commit()
    return order.id


def get_order_by_id(order_id: int) -> Order:
    order = Order.query.get(order_id)
    if order is None:
        return {"error": "Order with specified ID not found."}
    return {"status": order.status.name}
