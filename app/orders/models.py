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
        new_order = cls(quantity=quantity, product_id=product_id, status=status)
        db.session.add(new_order)
        db.session.commit()
        return new_order

    @staticmethod
    def get_status_choices():
        return [(status.value, status.value) for status in Order.DeliveryStatus]


class OrderAddress(db.Model):
    """
    Order address model
    """

    __table_name__ = "order_addresses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
