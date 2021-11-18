from myapp import myapp_obj
from myapp.forms import LoginForm, NoteForm
from flask import render_template, flash, redirect

from myapp import db
from myapp.models import User, Post, Note
from flask_login import current_user, login_user, logout_user, login_required

@myapp_obj.route("/loggedin")
@login_required
def log():
    return 'Hi you are logged in'

@myapp_obj.route("/logout")
def logout():
    logout_user()
    return redirect('/')

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Login invalid username or password!')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)
        flash(f'Login requested for user {form.username.data},remember_me={form.remember_me.data}')
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

@myapp_obj.route('/list-note', methods=['GET'])
def list_note():
    list_note = Note.query.all()
    return render_template('list-note.html', list_note=list_note)

@myapp_obj.route('/add-note', methods=['GET','POST'])
def add_note():
    form = NoteForm()
    if form.validate_on_submit():
        note = Note(title=form.title.data, description=form.description.data, content=form.content.data)
        db.session.add(note)
        db.session.commit()
        flash('The note is added')
        return redirect('/')
    return render_template('add-note.html', form=form)

@myapp_obj.route('/show-note/<id>', methods=['GET'])
def show_note(id):
    note = Note.query.get(int(id))
    return render_template('show-note.html', note=note)

@myapp_obj.route('/edit-note/<id>', methods=['GET','POST'])
def edit_note(id):
    form = NoteForm()
    note = Note.query.get(int(id))
    
    if form.validate_on_submit():
        note.title=form.title.data
        note.description=form.description.data
        note.content=form.content.data
        db.session.commit()
        return redirect('/show-note/' + id)
    
    form.title.data=note.title
    form.description.data=note.description
    form.content.data=note.content

    return render_template('edit-note.html', note=note, form=form)

@myapp_obj.route('/delete-note/<id>', methods=['GET','POST'])
def delete_note(id):
    note = Note.query.get(int(id))
    db.session.delete(note)
    db.session.commit()
    return redirect('/list-note')



