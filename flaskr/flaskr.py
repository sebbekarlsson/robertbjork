import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing
import yaml
from views.gallery import gallery
from views.contact import contact
from views.login import login
from views.index import index


with open("../config.yml", 'r') as stream:
            config = yaml.load(stream)

app = Flask(__name__)
app.config.from_object(__name__)

app.register_blueprint(index)
app.register_blueprint(gallery)
app.register_blueprint(contact)
app.register_blueprint(login)