
from flask import Blueprint, render_template
view = Blueprint('homepage', __name__)

@view.route('/')
def timeline():
    # Do some stuff
    return render_template("landing/landing.html")
