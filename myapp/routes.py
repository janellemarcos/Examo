from myapp import myapp_obj
from myapp.forms import LoginForm
from myapp.forms import RegisterForm
from flask import render_template, flash, redirect
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

    return render_template('hello.html', name=name, people=people, posts=posts)
