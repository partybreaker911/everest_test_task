from flask import render_template, request, redirect, url_for
from app import db
from app.products.models import Product
from app.products import products_blueprint


@products_blueprint.route("/", methods=["GET"])
def list_of_products():
    products = Product.query.all()
    return render_template(
        "templates/products/list_of_products.html", products=products
    )


@products_blueprint.route("/<int:product_id>", methods=["GET"])
def show_product(product_id):
    product = Product.query.get(product_id)
    return render_template("templates/products/show_product.html", product=product)
