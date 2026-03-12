from flask import Flask, request, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    id = StringField('id астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_captain = StringField('id капитана', validators=[DataRequired()])
    password_captain = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')