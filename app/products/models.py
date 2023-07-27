from app import db


class Product(db.Model):
    """DB model that stores all products"""

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float)
    color = db.Column(db.String(80))
    weight = db.Column(db.Float)
    description = db.Column(db.String(80))
    orders = db.relationship("Order", back_populates="product")

    def __init__(self, name, price, color, weight, description):
        self.name = name
        self.price = price
        self.color = color
        self.weight = weight
        self.description = description
