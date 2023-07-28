from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField
from wtforms.validators import DataRequired

from app.orders.models import Order


class OrderForm(FlaskForm):
    quantity = IntegerField("Quantity", validators=[DataRequired()])
    product_id = SelectField("Product", coerce=int)
    status = SelectField(
        "Status",
        choices=[(status.name, status.value) for status in Order.DeliveryStatus],
    )
