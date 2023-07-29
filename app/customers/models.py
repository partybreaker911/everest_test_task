from app import admin, db
from app.orders.models import Order
from app.customers.admin import CustomerAdmin, CustomerShippingAddressAdmin


class Customer(db.Model):
    """Model for customer."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    shipping_address = db.relationship(
        "CustomerShippingAddress",
        backref="customer",
        lazy="joined",
    )

    orders = db.relationship(Order, lazy="joined")

    def __repr__(self):
        """Represent this Customer as a string."""
        return f"<Customer id: {self.id}, customer name: {self.name}>"


class CustomerShippingAddress(db.Model):
    """Customer shipping address model"""

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("customer.id"),
        index=True,
        nullable=False,
    )
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    phone_number = db.Column(db.String(128), nullable=False)
    country = db.Column(db.String(128), nullable=False)
    city = db.Column(db.String(128), nullable=False)
    street = db.Column(db.String(128), nullable=False)
    house_number = db.Column(db.String(128), nullable=False)
    apartment_number = db.Column(db.String(128), nullable=False)
    postcode = db.Column(db.String(128), nullable=False)

    customers = db.relationship("Customer", lazy="joined")

    def __repr__(self):
        """Represent this CustomerShippingAddress as a string."""
        return f"<CustomerShippingAddress id: {self.id}, customer: {self.customer_id}>"


admin.add_view(
    CustomerAdmin(
        Customer,
        db.session,
        category="Customers",
    )
)

admin.add_view(
    CustomerShippingAddressAdmin(
        CustomerShippingAddress,
        db.session,
        category="Customers",
    )
)
