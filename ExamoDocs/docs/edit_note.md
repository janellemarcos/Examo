# def edit_note

	@myapp_obj.route('/edit-note/<id>', methods=['GET','POST'])
	@login_required
	def edit_note(id):
		"""
		Allows the authenticated user to edit their own notes. After saving the edited version, the user will be redirected to show the edited note.
			Parameters:
				id (int): the id of the note.
			Returns:
				render_template (method): the edit page for editing the user's note.
		"""
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
