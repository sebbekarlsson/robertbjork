from models import sess, User, Option
from flask import session, render_template
from sqlalchemy import update


def get_user(id):
    return sess.query(User).filter(User.id==id).first()

def only_admin():
    current_user = get_user(session.get('user'))

    if current_user == None:
        return render_template('notpermitted.html')
    else:
        if current_user.admin != 1:
            return render_template('notpermitted.html')

    return None

def get_users(offset, limit):
    return sess.query(User).limit(limit).offset(offset)

def unregister(id):
    sess.delete(get_user(id))
    sess.commit()

def make_admin(id):
    get_user(id).admin = 1
    sess.commit()

def remove_admin(id):
    get_user(id).admin = 0
    sess.commit()