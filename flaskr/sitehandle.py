from models import sess, Option

def get_option(key):
    return sess.query(Option).filter(Option.key==key).first()