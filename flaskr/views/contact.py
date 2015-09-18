from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


contact = Blueprint('contact', __name__,
                        template_folder='templates')

@contact.route('/contact')
def contact_blueprint():
    return render_template('contact.html')