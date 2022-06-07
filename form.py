from wtforms import Form
from wtforms import StringField, EmailField, PasswordField
from wtforms import validators

from models import User


class RegistroUsuarioForm(Form):
    username = StringField('Usuario', 
    [validators.length(min = 4, max = 8, message = 'Ingrese un usuario valido'), 
    validators.DataRequired(message = 'El usuario es requerido para el registro')])
    nombre = StringField('Nombre', 
    [validators.DataRequired(message = 'El nombre es requerido para el registro')])
    apellido = StringField('Apellido', 
    [validators.DataRequired(message = 'El apellido es requerido para el registro')])
    email = EmailField('Email', 
    [validators.Email(message = 'Ingrese un email valido'), 
    validators.DataRequired(message = 'El email es requerido para el registro')])
    password = PasswordField('Password',
    [validators.DataRequired(message = 'Ingrese su password' )])
    
    def validate_username(form, field):
        data = field.data
        user = User.query.filter_by(username = data).first()
        if user is not None:
            raise validators.ValidationError('El usuario ya fue registrado')
    def validate_email(form, field):
        data = field.data
        email = User.query.filter_by(email = data).first()
        if email is not None:
            raise validators.ValidationError('El correo ya fue registrado')

class LoginForm(Form):
    username = StringField('Usuario', 
    [validators.length(min = 4, max = 8, message = 'Ingrese un usuario valido'), 
    validators.DataRequired(message = 'Ingrese su usuario')])
    password = PasswordField('Password',
    [validators.DataRequired(message = 'Ingrese su password' )])
