from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from mylib.flickr import Flickr
from sitehandle import get_option


gallery = Blueprint('gallery', __name__,
                        template_folder='templates')

@gallery.route('/gallery/<page>')
def gallery_blueprint(page=1):
    flickr = Flickr(api_key=get_option('flickr_api_key').value, api_secret=\
        get_option('flickr_api_secret').value, api_farm=get_option('flickr_farm').value)

    photos = flickr.get_photos('robertbjork', page, 128)
    return render_template('gallery.html', photos=photos, page=page)