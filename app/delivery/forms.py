from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

from app.delivery.models import OrderStatusEnum
from app.catalog.models import Product


class OrderForm(FlaskForm):
    product = SelectField("Product", validators=[DataRequired()], coerce=str)
    quantity = IntegerField("Quantity", validators=[DataRequired()])
    address = StringField(
        "Delivery Address", validators=[DataRequired(), Length(max=255)]
    )
    submit = SubmitField("Submit Order")
