from app import db
from app.orders.models import Order
from app.orders.controller import create_order
from app.products.controller import get_product_by_id


def checkout_product(product_id: int, quantity: int) -> Order:
    """
    Create an order for a given product and quantity.

    Parameters:
        product_id (int): The ID of the product.
        quantity (int): The quantity of the product to be ordered.

    Returns:
        Order: An instance of the Order class representing the created order.

    Raises:
        None.

    Notes:
        This function first checks if the product with the given ID exists. If it does not, it returns a dictionary with the keys "success" (set to False) and "message" (set to "Product not found").

        If the product exists, this function creates an order with the specified quantity, product ID, and status set to "Pending". It then commits the changes to the database. Finally, it returns a dictionary with the keys "success" (set to True) and "message" (set to "Order placed successfully") to indicate the success of the operation.

        This function assumes that the necessary database session (`db.session`) is already available.

    Example:
        order = checkout_product(12345, 2)
    """
    product = get_product_by_id(product_id)

    if not product:
        return {"success": False, "message": "Product not found"}

    order = create_order(quantity=quantity, product_id=product.id, status="Pending")
    db.session.commit()
    return {"success": True, "message": "Order placed successfully"}
