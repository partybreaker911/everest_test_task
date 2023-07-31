import enum
import datetime

from app import db, admin
from app.addresses.models import (
    Country,
    City,
    Street,
)
from app.delivery.admin import (
    OrderAdmin,
    OrderDetailAdmin,
    OrderAddressAdmin,
)


class OrderStatusEnum(enum.Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELED = "Canceled"


# Define the association table for Order and OrderDetail
order_detail_association = db.Table(
    "order_detail_association",
    db.Column("order_id", db.Integer, db.ForeignKey("orders.id")),
    db.Column("order_detail_id", db.Integer, db.ForeignKey("order_details.id")),
    extend_existing=True,
)


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Enum(OrderStatusEnum), default=OrderStatusEnum.PENDING)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    # Define the many-to-many relationship with OrderDetail
    order_details = db.relationship(
        "OrderDetail", secondary=order_detail_association, back_populates="orders"
    )

    # One-to-One relationship with OrderAddress
    order_address = db.relationship(
        "OrderAddress", uselist=False, back_populates="order"
    )

    def __repr__(self):
        return f"<Order {self.id} - Status: {self.status}>"


class OrderDetail(db.Model):
    __tablename__ = "order_details"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer(), db.ForeignKey("products.id"))
    quantity = db.Column(db.Integer())

    # Define the many-to-many relationship with Order
    orders = db.relationship(
        "Order", secondary=order_detail_association, back_populates="order_details"
    )
    product = db.relationship("Product")

    def __repr__(self):
        return f"<OrderDetail {self.id} - Product: {self.product.name} - Quantity: {self.quantity}>"


class OrderAddress(db.Model):
    __tablename__ = "order_addresses"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer(), db.ForeignKey("orders.id"))
    address = db.Column(db.String(255))
    country_id = db.Column(db.Integer(), db.ForeignKey("countries.id"))
    city_id = db.Column(db.Integer(), db.ForeignKey("cities.id"))
    street_id = db.Column(db.Integer(), db.ForeignKey("streets.id"))

    # Many-to-One relationship with Country, City, and Street models
    country = db.relationship(Country, backref="order_addresses")
    city = db.relationship(City, backref="order_addresses")
    street = db.relationship(Street, backref="order_addresses")
    # One-to-One relationship with Order
    order = db.relationship("Order", back_populates="order_address")

    def __repr__(self):
        return f"<OrderAddress {self.id} - Address: {self.address}>"


admin.add_view(OrderAdmin(Order, db.session))
admin.add_view(OrderDetailAdmin(OrderDetail, db.session))
admin.add_view(OrderAddressAdmin(OrderAddress, db.session))
