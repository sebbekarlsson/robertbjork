import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing
import yaml
from views.gallery import gallery
from views.contact import contact
from views.login import login
from views.register import register
from views.index import index
from views.logout import logout


with open("../config.yml", 'r') as stream:
            config = yaml.load(stream)

app = Flask(__name__)
app.config.from_object(__name__)

app.secret_key = 'THIS_IS_VERY_SECRET'
app.config['SESSION_TYPE'] = 'filesystem'

app.register_blueprint(index)
app.register_blueprint(gallery)
app.register_blueprint(contact)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(register)
