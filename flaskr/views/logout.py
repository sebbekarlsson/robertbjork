from flask import Blueprint, render_template, abort, session
from jinja2 import TemplateNotFound


logout = Blueprint('logout', __name__,
                        template_folder='templates')

@logout.route('/logout')
def logout_blueprint():
    session.clear()
    return render_template('logout.html')