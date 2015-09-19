from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


login = Blueprint('login', __name__,
                        template_folder='templates')

class MyForm(Form):
    email = StringField('Email', validators=[Email(message=u'Invalid email address.')])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@login.route('/login', methods=('GET', 'POST'))
def login_blueprint():
    form = MyForm(csrf_enabled=False)
    form.validate_on_submit()
    return render_template('login.html', form=form)