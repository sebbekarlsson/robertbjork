from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from mylib.flickr import Flickr


gallery = Blueprint('gallery', __name__,
                        template_folder='templates')
flickr = Flickr()

@gallery.route('/gallery/<page>')
def gallery_blueprint(page=1):
    photos = flickr.get_photos('robertbjork', page, 128)
    return render_template('gallery.html', photos=photos, page=page)