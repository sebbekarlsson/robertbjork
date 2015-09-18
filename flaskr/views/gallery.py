from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from mylib.flickr import Flickr


gallery = Blueprint('gallery', __name__,
                        template_folder='templates')
flickr = Flickr()

@gallery.route('/gallery/<page>')
def flickr_gallery(page=1):
    photos = flickr.get_photos('robertbjork', page, 100, 't')
    return render_template('gallery.html', photos=photos)