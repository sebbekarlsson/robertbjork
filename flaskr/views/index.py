from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from sitehandle import get_option, get_flickr


index = Blueprint('index', __name__,
                        template_folder='templates')

@index.route('/')
def index_blueprint():
    bio_heading = get_option('bio_heading')
    bio = get_option('bio')

    flickr = get_flickr()
    flickr.get_galleries(get_option('flickr_user').value, 1, 100)
    photos = flickr.get_photos(get_option('flickr_user').value, 1, 28)

    return render_template('index.html', bio=bio, bio_heading=bio_heading, photos=photos)