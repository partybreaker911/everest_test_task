from app import db, admin
from app.catalog.admin import (
    CategoryAdmin,
    ProductAdmin,
    CategoryProductAdmin,
)


class Category(db.Model):
    """Category model"""

    __tablename__ = "categoryes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))

    def __repr__(self):
        return self.name


class Product(db.Model):
    """Product model"""

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    color = db.Column(db.String(100))
    weight = db.Column(db.Integer)

    def __repr__(self):
        return self.name


class CategoryProduct(db.Model):
    """CatalogProduct model"""

    __tablename__ = "category_products"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer(), db.ForeignKey("products.id"))
    category_id = db.Column(db.Integer(), db.ForeignKey("categoryes.id"))

    product = db.relationship("Product", backref="products")
    category = db.relationship("Category", backref="categories")

    def __repr__(self):
        return f"{self.product.name} - {self.category.name}"


admin.add_view(CategoryAdmin(Category, db.session, "Catalog"))
admin.add_view(ProductAdmin(Product, db.session, "Catalog"))
admin.add_view(CategoryProductAdmin(CategoryProduct, db.session, "Catalog"))
