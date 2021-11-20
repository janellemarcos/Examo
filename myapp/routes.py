from myapp import myapp_obj
from myapp.forms import LoginForm
from myapp.forms import RegisterForm
from flask import render_template, flash, redirect
from flask_login import current_user, login_user, logout_user, login_required
from myapp import db

@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return 'Hi ' + name

@myapp_obj.route("/")
def hello():
    name = 'Thomas'
    people = {'Carlos' : 54}
    title = 'My HommePage'
    posts = [{'author': 'john', 'body': 'Beautiful day in Portland!'},\
            {'author': 'Susan', 'body': 'Today was a good day!'}]

    return render_template('hello.html', authorized=current_user.is_authenticated, name=name, people=people, posts=posts)
