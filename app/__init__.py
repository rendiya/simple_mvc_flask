from flask import render_template, redirect, url_for, request, session
from flask import Flask
from flask import g
from flask import Response
from flask import request
from ayoklinik.controller.view import view
from ayoklinik.cache import cache

app = Flask(__name__)

app.config['CACHE_TYPE'] = 'simple'
cache.init_app(app)
app.config.from_pyfile('config.py')
app.register_blueprint(view, url_prefix='/')

