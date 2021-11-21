from myapp import myapp_obj
from myapp.forms import NoteForm, ShareForm
from flask import render_template, flash, redirect
from myapp import db
from sqlalchemy.exc import IntegrityError
from myapp.models import User, Note, UserNote
from flask_login import current_user, login_user, logout_user, login_required

@myapp_obj.route('/list-note', methods=['GET'])
@login_required
def list_note():
    list_note = current_user.notes
    return render_template('list-note.html', list_note=list_note, authorized=current_user.is_authenticated)

@myapp_obj.route('/add-note', methods=['GET','POST'])
@login_required
def add_note():
    form = NoteForm()
    if form.validate_on_submit():
        note = Note(title=form.title.data, description=form.description.data, content=form.content.data)
        current_user.notes.append(note)
        db.session.add(note)
        db.session.add(current_user)
        db.session.commit()
        flash('The note is added')
        return redirect('/')

    return render_template('add-note.html', form=form, authorized=current_user.is_authenticated)

@myapp_obj.route('/share-note/<id>', methods=['GET','POST'])
@login_required
def share_note(id):
    form = ShareForm()
    if form.validate_on_submit():
        note = Note.query.join(Note.users).filter(User.id==current_user.id, Note.id==id).first()
        if note == None:
            return redirect('/list-note')
        user = User.query.filter_by(username = form.username.data).first()
        user.notes.append(note)
        db.session.commit()
        flash('The note has been shared')
        return redirect('/list-note')

    return render_template('share-note.html', form=form, authorized=current_user.is_authenticated)

@myapp_obj.route('/show-note/<id>', methods=['GET'])
@login_required
def show_note(id):
    note = Note.query.join(Note.users).filter(User.id==current_user.id, Note.id==id).first()
    if note == None:
        return redirect('/list-note')

    return render_template('show-note.html', note=note, authorized=current_user.is_authenticated)

@myapp_obj.route('/edit-note/<id>', methods=['GET','POST'])
@login_required
def edit_note(id):
    form = NoteForm()
    note = Note.query.join(Note.users).filter(User.id==current_user.id, Note.id==id).first()
    if note == None:
        return redirect('/list-note')

    if form.validate_on_submit():
        note.title=form.title.data
        note.description=form.description.data
        note.content=form.content.data
        db.session.commit()
        return redirect('/show-note/' + id)

    form.title.data=note.title
    form.description.data=note.description
    form.content.data=note.content

    return render_template('edit-note.html', note=note, form=form, authorized=current_user.is_authenticated)

@myapp_obj.route('/delete-note/<id>', methods=['GET','POST'])
@login_required
def delete_note(id):
    note = Note.query.join(Note.users).filter(User.id==current_user.id, Note.id==id).first()
    if note == None:
        return redirect('list-note')

    note.users.remove(current_user)
    db.session.commit()
    return redirect('/list-note')
