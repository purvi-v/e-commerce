from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,IntegerField, TextAreaField,SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError,NumberRange
from market.models import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class AddItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30)])
    price = IntegerField('Price', validators=[DataRequired(), NumberRange(min=1)])
    barcode = StringField('Barcode', validators=[DataRequired(), Length(min=6, max=12)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=10, max=1024)])
    submit = SubmitField('Add Item')

class PurchaseItemForm(FlaskForm):
    purchased_item = SelectField('Item to Purchase')
    submit = SubmitField('Purchase')

class SellItemForm(FlaskForm):
    sold_item = SelectField('Item to Sell')
    submit = SubmitField('Sell') 