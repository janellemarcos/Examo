# def list_note

	@myapp_obj.route('/list-note', methods=['GET'])
	@login_required
	def list_note():
		"""
		Lists all the notes that the authenticated user made.
			Parameters:
				None
			Returns:
				render_template (method): unordered list of notes made by the user.
		"""
	    list_note = current_user.notes
	    return render_template('list-note.html', list_note=list_note, authorized=current_user.is_authenticated)
