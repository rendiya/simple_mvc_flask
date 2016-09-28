from flask import render_template, redirect, url_for, request, session
from flask import Flask
from flask import g
from flask import Response
from flask import request
from app.controller.view import view


app = Flask(__name__)

app.config.from_pyfile('config.py')
app.register_blueprint(view, url_prefix='/')

from app.controller.home import home #add
app.register_blueprint(home, url_prefix='/home') #add
from app.controller.rendi import rendi
app.register_blueprint(rendi, url_prefix='/rendi')
