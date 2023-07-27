from app import db


class Order(db.Model):
    """DB model that stores all orders"""

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    delivery_address_id = db.Column(db.Integer, db.ForeignKey("address.id"))
    quantity = db.Column(db.Integer, nullable=False)

    user = db.relationship("User", back_populates="orders")
    delivery_address = db.relationship("Address")
    product = db.relationship("Product", back_populates="orders")

    def __init__(self, user_id, product_id, quantity, delivery_address_id):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity
        self.delivery_address_id = delivery_address_id