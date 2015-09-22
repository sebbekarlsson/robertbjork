from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from mylib.flickr import Flickr
from sitehandle import get_option, get_flickr


gallery = Blueprint('gallery', __name__,
                        template_folder='templates')

@gallery.route('/gallery/<page>')
def gallery_blueprint(page=1):
    flickr = get_flickr()

    photos = flickr.get_photos(get_option('flickr_user').value, page, 128)
    return render_template('flickr_gallery.html', photos=photos, page=page, base_url='/gallery/')