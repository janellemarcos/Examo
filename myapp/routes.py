from myapp import myapp_obj
from myapp.forms import LoginForm
from flask import render_template, flash, redirect

from myapp import db
from myapp.models import User
from flask_login import current_user, login_user, logout_user, login_required

@myapp_obj.route("/delete")
@login_required
def delete():
    #get logged in user data (could be id, username) 
    #save user to variable u
    #call u.query.filter_by(id).delete()
    #Ref: https://flask-login.readthedocs.io/en/latest/

@myapp_obj.route("/logout")
def logout():
    #no change here, can just call logout
    logout_user()
    return redirect('/')

@myapp_obj.route("/register", methods=['GET', 'POST'])
def register():
    db.create_all()
    usernames = User.query.all()
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data is None or form.password.data is None:
            return redirect('/')
        p = User(username=form.username.data, password=form.password.data)
        db.session.add(p)
        db.session.commit()
        return redirect('/')
    return render_template('register.html', form=form)


@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    # will replace flash with something else later on
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Login invalid username or password!')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)
        flash(f'Login requested for user {form.username.data}')
        flash(f'Login password {form.password.data}')
        return redirect('/')
    return render_template("login.html", form=form)


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
