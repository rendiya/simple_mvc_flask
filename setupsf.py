import os,sys
def pilihmenu():
    print "welcome to setup simple flask mvc"
    print "1) create simple controller"
    input_var = raw_input("enter menu : ")
    try:
        input_var = int(input_var)
    except Exception:
        print "salah input"
    if input_var == 1:
        print ("create your controller")
        input_name = raw_input("enter controller : ")
        createcontroller(input_name)
    else:
        pilihmenu()
def createcontroller(name):
    print "your controller name is %s.py" % name
    with open('app/controller/%s.py' % name, 'w') as file:
        file.write('''
from flask import Blueprint, render_template
%(s)s = Blueprint('newbot', __name__)
@%(s)s.route('/')
def newbot():
	return render_template("landing/landing.html")
''' % {'s': name})
    with open('app/__init__.py', "a") as file:
        file.write('''
from app.controller.%(s)s import %(s)s
app.register_blueprint(%(s)s, url_prefix='/%(s)s')
'''% {'s': name})
    



pilihmenu()