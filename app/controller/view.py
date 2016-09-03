
from flask import Blueprint, render_template
from ayoklinik.cache import cache
view = Blueprint('profile', __name__)

@view.route('/')
@cache.cached(timeout=60)
def timeline():
    # Do some stuff
    return render_template("landing/landing.html")
