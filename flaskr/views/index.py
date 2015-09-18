from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


index = Blueprint('index', __name__,
                        template_folder='templates')

@index.route('/')
def index_blueprint():
    return render_template('index.html')