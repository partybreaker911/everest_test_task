from flask import render_template, redirect, url_for
from flask_security import roles_required

from app.catalog import catalog_blueprint
from app.catalog.forms import ProductForm
from app.catalog.controller import (
    get_all_categoryes,
    get_all_products,
    get_product,
    create_product,
    delete_product,
)


@catalog_blueprint.route("/", methods=["GET"])
def list_of_all_categoryes():
    categoryes = get_all_categoryes()
    return render_template("catalog/list_of_categoryes.html", categoryes=categoryes)


@catalog_blueprint.route("/products", methods=["GET"])
def list_of_all_products():
    products = get_all_products()
    return render_template("catalog/list_of_products.html", products=products)


@catalog_blueprint.route("/products/<int:id>/detail", methods=["GET"])
def get_product_view(id):
    product = get_product(id)
    return render_template("catalog/product_detail.html", product=product)


@roles_required("admin")
@catalog_blueprint.route("/products/create", methods=["GET", "POST"])
def add_product():
    form = ProductForm()

    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        color = form.color.data
        weight = form.weight.data

        new_product = create_product(name=name, price=price, color=color, weight=weight)
        return redirect(
            url_for("catalog.list_of_all_products")
        )  # Redirect to a page showing a list of products

    return render_template("catalog/create_product.html", form=form)


@roles_required("admin")
@catalog_blueprint.route("/products/<int:id>/delete", methods=["GET", "POST"])
def product_delete(id):
    delete_product(id)
    return redirect(url_for("catalog.list_of_all_products"))
