from app import db, admin
from app.products.admin import ProductAdmin, CategoryAdmin


class Category(db.Model):
    """Model for product category."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(length=140),
        index=True,
        unique=True,
        nullable=False,
    )
    description = db.Column(db.Text)

    parent_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    parent = db.relationship("Category", remote_side=id, backref="subcategories")

    def __repr__(self):
        return self.name


class Product(db.Model):
    """
    Product model
    """

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    price = db.Column(db.DECIMAL(10, 2), default=0.0)
    color = db.Column(db.String(128), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)

    # orders = db.relationship("Order", backref="products")

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


class ProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))

    product = db.relationship("Product", lazy="joined")
    category = db.relationship("Category", lazy="joined")


admin.add_view(ProductAdmin(Product, db.session))
admin.add_view(CategoryAdmin(Category, db.session))
