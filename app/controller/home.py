#add file
from flask import Blueprint, render_template #tetap
home = Blueprint('home', __name__) #berubah

@home.route('/') #berubah di sebelum titik
def timeline():
    return render_template("landing/landing.html")
