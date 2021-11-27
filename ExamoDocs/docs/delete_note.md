# def delete_note

	@myapp_obj.route('/delete-note/<id>', methods=['GET','POST'])
	@login_required
	def delete_note(id):
		"""
		Deletes the specified note by the user.
			Parameters:
				id (int): the id of the note.
			Returns:
				redirect (method): redirects the user back to their updated list of notes.

		"""
	    note = Note.query.join(Note.users).filter(User.id==current_user.id, Note.id==id).first()
	    if note == None:
	        return redirect('list-note')

	    note.users.remove(current_user)
	    db.session.commit()
	    return redirect('/list-note')