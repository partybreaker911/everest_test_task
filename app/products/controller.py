from app import db
from app.products.models import Product


def create_product(
    name: str, price: float, color: str, weight: float, description: str
) -> None:
    """
    Create a product and save it to the database.

    Args:
        name: The name of the product.
        price: The price of the product.
        color: The color of the product.
        weight: The weight of the product.
        description: The description of the product.

    Returns:
        None
    """
    product = Product(name, price, color, weight, description)
    db.session.add(product)
    db.session.commit()


def update_product(
    product_id: int,
    name: str,
    price: float,
    color: str,
    weight: float,
    description: str,
) -> None:
    """
    Updates the details of a product in the database.

    Args:
        product_id: The ID of the product to be updated.
        name: The new name of the product.
        price: The new price of the product.
        color: The new color of the product.
        weight: The new weight of the product.
        description: The new description of the product.

    Returns:
        None
    """
    product = Product.query.get(product_id)
    product.name = name
    product.price = price
    product.color = color
    product.weight = weight
    product.description = description
    db.session.commit()


def delete_product(product_id: int) -> None:
    """
    Deletes a product from the database.

    Args:
        product_id (int): The ID of the product to be deleted.

    Returns:
        None
    """
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()
