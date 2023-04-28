from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from forms import LoginForm

class LoginForm(FlaskForm):
    username = StringField('Username', [validators.InputRequired()])
    password = PasswordField('Password', [validators.InputRequored()])


    