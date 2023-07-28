from typing import List, Any, Optional

from app import db
from app.orders.models import Order
from app.products.controller import product_view


def order_list() -> List[str]:
    """
    Retrieve a list of orders from the database.

    Returns:
        A list of order objects.
    """
    orders = Order.query.all()
    return orders


def order_view(id: int) -> Any:
    """
    Retrieve an order by its ID.

    Args:
        id (int): The ID of the order.

    Returns:
        Any: The order object if found.

    Raises:
        404: If the order with the given ID does not exist.
    """
    order = Order.query.get_or_404(id)
    return order


def order_create(quantity: int, product_id: int) -> Optional[Order]:
    """
    Create a new order in the database.

    Args:
        quantity (int): The quantity of the product in the order.
        product_id (int): The ID of the product associated with the order.

    Returns:
        Order: The newly created order object.
    Raises:
        ValueError: If the product with the given ID does not exist.
    """
    try:
        # Получите объект продукта по ID
        product = product_view(product_id)
    except ValueError:
        raise ValueError("Product not found")

    # Создайте новый заказ
    new_order = Order(quantity=quantity, product=product)
    db.session.add(new_order)
    db.session.commit()

    return new_order


def order_update(id: int, quantity: float) -> Optional[Order]:
    """
    Update the quantity of an existing order.

    Args:
        id (int): The ID of the order.
        quantity (float): The new quantity for the order.

    Returns:
        Optional[Order]: The updated order, or None if there was an error.
    """
    try:
        order = Order.query.get_or_404(id)
        order.quantity = quantity
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
