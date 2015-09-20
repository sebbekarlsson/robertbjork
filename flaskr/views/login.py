from flask import Blueprint, render_template, abort, request, session, url_for, redirect
from jinja2 import TemplateNotFound

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from models import sess, User


login = Blueprint('login', __name__,
                        template_folder='templates')

class MyForm(Form):
    email = StringField('Email', validators=[Email(message=u'Invalid email address.')])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@login.route('/login', methods=('GET', 'POST'))
def login_blueprint():

    if session.get('user') != None:
        return redirect('/')

    form = MyForm(csrf_enabled=False)
    msg = ''

    if form.validate_on_submit():
        fetched_user = sess.query(User).filter(User.email==form.email.data).first()
        
        if fetched_user.password != form.password.data:
            session.clear()
            msg = 'Wrong password'
        else:
            if fetched_user.password == form.password.data:
                session['user'] = fetched_user.id
                session['loggedin'] = True
                
                return redirect('/')

    return render_template('login.html', form=form, msg=msg)