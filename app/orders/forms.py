from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired

from app.orders.models import Order
from app.products.models import Product


class OrderForm(FlaskForm):
    quantity = IntegerField("Quantity", validators=[DataRequired()])
    product_id = SelectField("Product", coerce=int, validators=[DataRequired()])
    status = SelectField("Status", choices=[], validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.product_id.choices = [
            (product.id, product.name) for product in Product.query.all()
        ]
        self.status.choices = Order.get_status_choices()

    def validate(self):
        if not super(OrderForm, self).validate():
            return False

        return True


class AddressForm(FlaskForm):
    country_id = SelectField("Country", coerce=int, validators=[DataRequired()])
    city_id = SelectField("City", coerce=int, validators=[DataRequired()])
    street_id = SelectField("Street", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Submit Address")
