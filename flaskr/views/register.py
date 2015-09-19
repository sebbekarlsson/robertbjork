from flask import Blueprint, render_template, abort, request, flash
from jinja2 import TemplateNotFound

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from models import sess, User


register = Blueprint('register', __name__,
                        template_folder='templates')

class MyForm(Form):
    email = StringField('Email', validators=[Email(message=u'Invalid email address.')])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

@register.route('/register', methods=('GET', 'POST'))
def register_blueprint():
    form = MyForm(csrf_enabled=False)

    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        sess.add(user)
        sess.commit()
        flash('Thank you for registering!')

    return render_template('register.html', form=form)