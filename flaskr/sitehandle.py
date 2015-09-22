from models import sess, Option
from mylib.flickr import Flickr


def get_option(key):
    return sess.query(Option).filter(Option.key==key).first()

def get_options(offset, limit):
    return sess.query(Option).offset(offset).limit(limit)

def create_option(key, value):
    sess.add(Option(key=key, value=value))
    sess.commit()

def delete_option(key):
    sess.delete(get_option(key))
    sess.commit()

def get_flickr():
    return Flickr(api_key=get_option('flickr_api_key').value, api_secret=\
        get_option('flickr_api_secret').value, api_farm=get_option('flickr_farm').value)