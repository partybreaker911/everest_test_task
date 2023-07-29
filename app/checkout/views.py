from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    request,
)

from . import checkout_blueprint
from app.checkout.controller import checkout_product


@checkout_blueprint.route("/checkout/<int:product_id>", methods=["POST"])
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
    quantity = int(request.form.get("quantity", 1))  # Get the quantity from the form

    result = checkout_product(product_id, quantity)

    if result["success"]:
        flash(result["message"], "success")
    else:
        flash(result["message"], "error")
        return redirect(url_for("products.view_product", product_id=product_id))

    return render_template("checkout/checkout_success.html", product_id=product_id)
