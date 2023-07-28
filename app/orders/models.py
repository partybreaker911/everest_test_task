from datetime import datetime

from app import db
from app.orders.utils.enum import DeliveryStatus


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(100))
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer)

    def __init__(self, quantity, product_id):
        # self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity
        # self.delivery_address_id = delivery_address_id
