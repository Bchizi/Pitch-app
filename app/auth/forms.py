from flask_wtf import FlaskForm
from wtforms import PasswordField,SubmitField,ValidationError,StringField,BooleanField
from wtforms.validators import DataRequired, Email,EqualTo
from ..models import User,Pitch

class RegistrationForm(FlaskForm):
    email = StringField('Your email Address', validators=[DataRequired(),Email()])
    username = StringField('Enter your Username', validators=[DataRequired(),])
    password = PasswordField('password', validators = [DataRequired(),EqualTo('confirm_password',message= 'the two passwords shoukd be equal')])
    confirm_password = PasswordField('Confirm password',validators = [DataRequired()])
    submit = SubmitField('SignUp')

    def validate_email(self,email):
        if User.query.filter_by(email = email.data).first():
            raise ValidationError('The Email enterd already exists please Login or use another Email!')
    def validate_username(self,username):
        if User.query.filter_by(username= username.data).first():
            raise ValidationError('Name already exists please')


class LoginForm(FlaskForm):
    email = StringField('Email...',validators=[DataRequired(),Email()])
    password= PasswordField('password...',validators=[DataRequired()])
    remember = BooleanField('remember me')
    submit= SubmitField('Sign In')

        


