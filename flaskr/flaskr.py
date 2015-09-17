import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing
from mylib.flickr import Flickr

    
DATABASE = '/tmp/robertbjork.db'
DEBUG = True
USERNAME = 'root'
PASSWORD = 'tango255'

flickr = Flickr()

app = Flask(__name__)
app.config.from_object(__name__)

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def index():
    image_urls = flickr.get_photos('robertbjork', 1, 100, 'm')
    return render_template('index.html', image_urls=image_urls)

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()