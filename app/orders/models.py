import enum
from datetime import datetime

from app import db
from app.products.models import Product


class OrderStatusEnum(enum.Enum):
    """Class for choosing order statuses"""

    processed = "processed"
    unprocessed = "unprocessed"


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(
        db.Enum(OrderStatusEnum), default=OrderStatusEnum.unprocessed, nullable=False
    )
    delivered_at = db.Column(db.DateTime)


class OrderProduct(db.Model):
    """Model for product order"""

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(
        db.Integer,
        db.ForeignKey("order.id"),
        index=True,
        nullable=False,
    )
    product_id = db.Column(
        db.Integer,
        db.ForeignKey("product.id"),
        index=True,
        nullable=False,
    )
    quantity = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.DECIMAL(10, 2), default=0.0)

    order = db.relationship("Order", lazy="joined")
    product = db.relationship(Product, lazy="joined")

    __table_args__ = (
        db.CheckConstraint(
            quantity >= 0,
            name="quantity_positive_or_zero",
        ),
        db.CheckConstraint(
            cost >= 0,
            name="check_order_product_cost_non_negative",
        ),
        {},
    )

    def __repr__(self):
        """Represent this OrderProduct as a string."""
        return f"<OrderProduct order: {self.order_id} product: {self.product_id}>"
