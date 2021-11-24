# def add_note

	@myapp_obj.route('/add-note', methods=['GET','POST'])
	@login_required
	def add_note():
		"""
		Allows the authenticated user to add a note with their desired title, description, and content. A message will appear if the note has been successfully added.
			Parameters:
				None
			Returns:
				redirect (method): lists all the notes made by the user.
		"""
	    form = NoteForm()
	    if form.validate_on_submit():
	        note = Note(title=form.title.data, description=form.description.data, content=form.content.data)
	        current_user.notes.append(note)
	        db.session.add(note)
	        db.session.add(current_user)
	        db.session.commit()
	        flash('The note is added')
	        return redirect('/list-note')