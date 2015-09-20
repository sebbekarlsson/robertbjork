from flask import Blueprint, render_template, abort, session, request
from jinja2 import TemplateNotFound
from userhandle import get_user, get_users, only_admin, make_admin, remove_admin, unregister


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

    users = get_users(offset=page*10, limit=10)

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


    return render_template('admin_users.html', users=users)

admin_meta = Blueprint('admin_meta', __name__,
                        template_folder='templates')

@admin_meta.route('/admin/meta')
def admin_meta_blueprint():
    if only_admin() != None:
        return only_admin()

    return render_template('admin_meta.html')


admin_flickr = Blueprint('admin_flickr', __name__,
                        template_folder='templates')

@admin_flickr.route('/admin/flickr')
def admin_flickr_blueprint():
    if only_admin() != None:
        return only_admin()

    return render_template('admin_flickr.html')