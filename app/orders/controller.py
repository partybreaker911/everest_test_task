from typing import List, Any, Optional

from app import db
from app.orders.models import Order


def order_list() -> List[str]:
    """
    Retrieve a list of orders from the database.

    Returns:
        A list of order objects.
    """
    orders = Order.query.all()
    return orders


def get_order_by_id(order_id: int) -> Any:
    """
    Retrieve an order by its ID.

    Args:
        id (int): The ID of the order.

    Returns:
        Any: The order object if found.

    Raises:
        404: If the order with the given ID does not exist.
    """
    order = Order.query.get_or_404(order_id)
    return order


def create_order(quantity: int, product_id: int, status: str):
    status_enum = Order.DeliveryStatus(status)
    return Order.create_order(
        quantity=quantity, product_id=product_id, status=status_enum
    )


def order_update(
    order_id: int, quantity: int, product_id: int, status: str
) -> Optional[Order]:
    """
    Update the quantity, product_id, and status of an existing order.

    Args:
        order_id (int): The ID of the order.
        quantity (int): The new quantity for the order.
        product_id (int): The new product_id for the order.
        status (str): The new status for the order.

    Returns:
        Optional[Order]: The updated order, or None if there was an error.
    """
    try:
        order = get_order_by_id(order_id)
        order.quantity = quantity
        order.product_id = product_id
        order.status = status
        db.session.commit()
        return order
    except Exception:
        return None


def order_delete(id: int) -> Optional[Order]:
    """
    Delete an existing order.

    Args:
        id (int): The ID of the order.

    Returns:
        Optional[Order]: The deleted order, or None if there was an error.
    """
    try:
        order = Order.query.get_or_404(id)
        db.session.delete(order)
        db.session.commit()
        return order
    except Exception:
        return None
