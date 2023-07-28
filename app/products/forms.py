from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange
from wtforms import StringField, FloatField, TextAreaField, SubmitField


class ProductForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    price = FloatField("Price", validators=[DataRequired(), NumberRange(min=0)])
    color = StringField("Color", validators=[DataRequired()])
    weight = FloatField("Weight", validators=[DataRequired(), NumberRange(min=0)])
    description = TextAreaField("Description", validators=[DataRequired()])
    submit = SubmitField("Submit")
