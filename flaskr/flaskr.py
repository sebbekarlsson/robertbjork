import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing
import yaml
from views.gallery import gallery


with open("../config.yml", 'r') as stream:
            config = yaml.load(stream)

DATABASE = '/tmp/robertbjork.db'
DEBUG = True
USERNAME = 'root'
PASSWORD = 'tango255'

app = Flask(__name__)
app.config.from_object(__name__)

app.register_blueprint(gallery)

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
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')
