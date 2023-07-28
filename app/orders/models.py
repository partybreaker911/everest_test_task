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


class OrderAddress(db.Model):
    """
    Order address model
    """

    __table_name__ = "order_addresses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
