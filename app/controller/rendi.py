
from flask import Blueprint, render_template
rendi = Blueprint('newbot', __name__)
@rendi.route('/')
def newbot():
	return render_template("landing/landing.html")
