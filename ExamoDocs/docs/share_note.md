# def share_note

	@myapp_obj.route('/share-note/<id>', methods=['GET','POST'])
	@login_required
	def share_note(id):
		"""
		Allows the authenticated user to share their notes among other valid users. A message will appear if sharing the notes is successful.
			Parameters:
				id (int): the id of the note.
			Returns:
				redirect (method): redirects user to their list of notes.
		"""
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