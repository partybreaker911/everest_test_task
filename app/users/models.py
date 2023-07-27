from app import db


class User(db.Model):
    """DB model that stores all users"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    current_address_id = db.Column(db.Integer, db.ForeignKey("address.id"))

    def __init__(self, username, email, *args, **kwargs):
        self.username = username
        self.email = email


class Address(db.Model):
    """DB model that stores all addresses"""

    __tablename__ = "address"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street = db.Column(db.String)
    city = db.Column(db.String)
    country = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="delivery_addresses")
