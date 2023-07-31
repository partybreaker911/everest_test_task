"""
IDK is it right to create this in Flask but if we using MVC pattern so we need this
"""
from typing import List

from app import db
from app.catalog.forms import ProductForm
from app.catalog.models import Category, Product


def get_all_categoryes() -> List[Category]:
    return db.session.query(Category).all()


def get_all_products() -> List[Product]:
    return db.session.query(Product).all()


def create_product(name: str, price: float, color: str, weight: int) -> Product:
    new_product = db.session.execute(
        Product.__table__.insert().values(
            name=name,
            price=price,
            color=color,
            weight=weight,
        )
    )
    db.session.commit()
    return new_product


def delete_product(id: int) -> None:
    db.session.execute(Product.__table__.delete().where(Product.id == id))
    db.session.commit()


def get_product(id: int) -> Product:
    return db.session.query(Product).filter(Product.id == id).first()
