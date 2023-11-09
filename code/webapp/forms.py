from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, Email


class OrderForm(FlaskForm):
    firstname = StringField("Your first name", validators=[InputRequired()])
    surname = StringField("Your surname", validators=[InputRequired()])
    email = StringField(
        "Your Email Address",
        validators=[InputRequired(), Email(message="Invalid email address")],
    )
    shipping_address = StringField("Shipping Address", validators=[InputRequired()])
    submit = SubmitField("Send order to Warehouse!!")


class SearchForm(FlaskForm):
    search_query = StringField("Search")
    submit = SubmitField("Search")
