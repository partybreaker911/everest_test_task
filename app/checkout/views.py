from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    request,
)

from . import checkout_blueprint
from app.checkout.forms import CheckoutForm
from app.checkout.controller import checkout_product
from app.products.controller import get_product_by_id


@checkout_blueprint.route("/checkout/<int:product_id>", methods=["POST", "GET"])
def checkout(product_id: int) -> None:
    """
    Checkout the specified product.

    Parameters:
    - product_id (int): The ID of the product to be checked out.

    Returns:
    - None

    Raises:
    - RedirectException: If the checkout is unsuccessful and the user needs to be redirected.

    This function handles the checkout process for a specific product. It retrieves the quantity from the form data and calls the `checkout_product` function to perform the checkout. If the checkout is successful, a success message is flashed to the user. Otherwise, an error message is flashed and the user is redirected to the product view page. The function then renders the template for the successful checkout, passing in the product ID.

    Note: You can customize the template name for the checkout success page.
    """
    product = get_product_by_id(product_id)
    form = CheckoutForm()
    if form.validate_on_submit():
        quantity = form.quantity.data

        result = checkout_product(product_id, quantity)

        if result["success"]:
            flash(result["message"], "success")
            return redirect(url_for("checkout.checkout_success"))
        else:
            flash(result["message"], "error")

    return render_template("checkout/checkout.html", product=product, form=form)


@checkout_blueprint.route("/checkout/success", methods=["GET"])
def checkout_success() -> None:
    return "OK"
