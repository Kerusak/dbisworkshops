from wtforms import Form
from wtforms import StringField, SubmitField
import wtforms
from wtforms.validators import DataRequired, EqualTo


class RegisterForm(Form):
    fname = StringField("fname", validators=[DataRequired("Please enter your first name")])

    mname = StringField("mname", validators=[DataRequired("Please enter your middle name")])

    lname = StringField("lname", validators=[DataRequired("Please enter your last name")])

    email = StringField("email", validators=[DataRequired("Please enter your email address.")])

    password = wtforms.PasswordField("password", validators=[DataRequired("Please enter your password."),
                                                             EqualTo('repeat', message='Password must much')])

    repeat = wtforms.PasswordField("repeat", validators=[DataRequired("Please repeat password.")])

    submit = SubmitField("Register")
