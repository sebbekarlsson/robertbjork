from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


login = Blueprint('login', __name__,
                        template_folder='templates')

@login.route('/login')
def login_blueprint():
    return render_template('login.html')