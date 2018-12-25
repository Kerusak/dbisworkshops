from wtforms import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(Form):
    email = StringField("Email", validators=[DataRequired("Please enter your email address.")])

    password = StringField("Password", validators=[DataRequired("Please enter your login.")])

    submit = SubmitField("Send")
