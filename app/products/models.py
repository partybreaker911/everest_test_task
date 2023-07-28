from app import db


class Product(db.Model):
    """
    Product model
    """

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    color = db.Column(db.String(128), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)

    orders = db.relationship("Order", backref="products")

    def __repr__(self):
        return "<Product %r>" % self.name

    def serialize(self):
        return dict(
            id=self.id,
            name=self.name,
            price=self.price,
            color=self.color,
            weight=self.weight,
            description=self.description,
        )
