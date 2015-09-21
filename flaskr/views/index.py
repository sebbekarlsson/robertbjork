from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from models import sess, Option


index = Blueprint('index', __name__,
                        template_folder='templates')

@index.route('/')
def index_blueprint():
    bio = sess.query(Option).filter(Option.key=='bio').first()
    return render_template('index.html', bio=bio)