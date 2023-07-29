from datetime import datetime
from enum import Enum

from app import db


class Order(db.Model):
    """
    Order model
    """

    class DeliveryStatus(Enum):
        PENDING = "Pending"
        DELIVERED = "Delivered"
        CANCELLED = "Cancelled"

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantity = db.Column(db.Integer)
    status = db.Column(db.Enum(DeliveryStatus), default=DeliveryStatus.PENDING)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    product = db.relationship("Product", backref="orders_relation")
    created_at = db.Column(db.DateTime, default=datetime.now)

    @classmethod
    def create_order(cls, quantity: int, product_id: int, status: str):
        """
        Create an order with the given quantity, product ID, and status.

        Args:
            quantity (int): The quantity of the order.
            product_id (int): The ID of the product.
            status (str): The status of the order.

        Returns:
            Order: The newly created order.
        """
        new_order = cls(quantity=quantity, product_id=product_id, status=status)
        db.session.add(new_order)
        db.session.commit()
        return new_order

    @staticmethod
    def get_status_choices():
        """
        This static method returns the choices for the status field in the Order model.

        Returns:
            list: A list of tuples containing the status value as both the key and the value.
        """
        return [(status.value, status.value) for status in Order.DeliveryStatus]


class OrderAddress(db.Model):
    """Model that stores order address information."""

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    order = db.relationship("Order", backref=db.backref("address", uselist=False))
    country_id = db.Column(db.Integer, db.ForeignKey("country.id"), nullable=False)
    country = db.relationship(
        "Country", backref=db.backref("order_addresses", lazy=True)
    )
    city_id = db.Column(db.Integer, db.ForeignKey("city.id"), nullable=False)
    city = db.relationship("City", backref=db.backref("order_addresses", lazy=True))
    street_id = db.Column(db.Integer, db.ForeignKey("street.id"), nullable=False)
    street = db.relationship("Street", backref=db.backref("order_addresses", lazy=True))

    def __init__(self, country, region, city, street):
        self.country = country
        self.region = region
        self.city = city
        self.street = street
