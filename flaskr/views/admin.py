from flask import Blueprint, render_template, abort, session, request
from jinja2 import TemplateNotFound
from userhandle import get_user, get_users, only_admin, make_admin, remove_admin, unregister

from sitehandle import get_option

from flask_wtf import Form
from wtforms import TextAreaField, SubmitField, SelectField, StringField
from wtforms.validators import DataRequired, Email

from models import sess


admin = Blueprint('admin', __name__,
                        template_folder='templates')

@admin.route('/admin/')
def admin_blueprint():
    only_admin()
    return render_template('admin.html')


admin_users = Blueprint('admin_users', __name__,
                        template_folder='templates')

@admin_users.route('/admin/users/<page>', methods=['POST', 'GET'])
def admin_users_blueprint(page=0):
    if only_admin() != None:
        return only_admin()

    users = get_users(offset=int(page)*10, limit=10)

    selected_user = request.form.get('selected_user')
    mk_admin = request.form.get('make_admin')
    rm_admin = request.form.get('remove_admin')
    delete = request.form.get('delete')

    if mk_admin != None:
        make_admin(selected_user)

    if rm_admin != None:
        remove_admin(selected_user)

    if delete != None:
        unregister(selected_user)


    return render_template('admin_users.html', users=users, page=page)

admin_meta = Blueprint('admin_meta', __name__,
                        template_folder='templates')

class BioForm(Form):
    bio = TextAreaField('Bio')
    submit = SubmitField('Update')

@admin_meta.route('/admin/meta', methods=['POST', 'GET'])
def admin_meta_blueprint():
    if only_admin() != None:
        return only_admin()

    bioform = BioForm(csrf_enabled=False)
    msg = ''

    if bioform.validate_on_submit():
        get_option('bio').value = bioform.bio.data
        sess.commit()
    else:
        bioform.bio.data = get_option('bio').value

    return render_template('admin_meta.html', bioform=bioform, msg=msg)


admin_flickr = Blueprint('admin_flickr', __name__,
                        template_folder='templates')

class FlickrForm(Form):
    farm = SelectField("Farm", coerce=int, choices=[(i, i) for i in range(1, 10)], default=2)
    apikey = StringField("Api Key")
    apisecret = StringField("Api Secret")
    submit = SubmitField('Update')


@admin_flickr.route('/admin/flickr', methods=['GET', 'POST'])
def admin_flickr_blueprint():
    if only_admin() != None:
        return only_admin()

    flickrform = FlickrForm(csrf_enabled=False)
    msg = ''

    if flickrform.validate_on_submit():
        get_option('flickr_api_key').value = flickrform.apikey.data
        get_option('flickr_api_secret').value = flickrform.apisecret.data
        get_option('flickr_farm').value = flickrform.farm.data

        sess.commit()
    else:
        flickrform.apikey.data = get_option('flickr_api_key').value
        flickrform.apisecret.data = get_option('flickr_api_secret').value
        flickrform.farm.data = int(get_option('flickr_farm').value)


    return render_template('admin_flickr.html', flickrform=flickrform)

