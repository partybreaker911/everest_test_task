from typing import List, Any

from app import db
from app.products.models import Product


def product_list() -> List[str]:
    """
    Retrieves a list of all products from the database.

    Returns:
        List[str]: A list of all products in the database.
    """
    products = Product.query.all()
    return products


def product_view(id: int) -> Any:
    """
    Get a product by its ID.

    Args:
        id (int): The ID of the product.

    Returns:
        Any: The product object.
    """
    product = Product.query.get_or_404(id)
    return product


def product_create(
    name: str, price: float, color: str, weight: float, description: str
) -> Any:
    """
    Create a new product in the database.

    Args:
        name: The name of the product (str)
        price: The price of the product (float)
        color: The color of the product (str)
        weight: The weight of the product (float)
        description: The description of the product (str)

    Returns:
        The newly created product (Any)
    """
    new_product = Product(
        name=name, price=price, color=color, weight=weight, description=description
    )
    db.session.add(new_product)
    db.session.commit()
    return new_product


def product_update(
    id: int, name: str, price: float, color: str, weight: float, description: str
) -> Any:
    """
    Update product information in the database.

    Args:
        id (int): The ID of the product to be updated.
        name (str): The new name of the product.
        price (float): The new price of the product.
        color (str): The new color of the product.
        weight (float): The new weight of the product.
        description (str): The new description of the product.

    Returns:
        Any: The updated product object.
    """
    product = Product.query.get_or_404(id)
    product.name = name
    product.price = price
    product.color = color
    product.weight = weight
    product.description = description
    db.session.commit()
    return product


def product_delete(id: int) -> bool:
    """
    Deletes a product from the database.

    Args:
        id: The ID of the product to be deleted.

    Returns:
        True if the product is successfully deleted, False otherwise.
    """
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return True
