# def list_note

	@myapp_obj.route('/list-note', methods=['GET'])
	@myapp_obj.route('/list-note/<sort_option>', methods=['GET'])
	@login_required
	def list_note(sort_option):
		"""
		Lists all the notes that the authenticated user made.
			Parameters:
				sort_option (String): sorting option
			Returns:
				render_template (method): unordered list of notes made by the user.
		"""
	    list_note = current_user.notes
		sorted_notes = list_note
		if sort_option == 'ascending':
			sorted_notes = sorted(list_note, key=lambda d: d.title)
		elif sort_option =='descending':
			sorted_notes = sorted(list_note, key=lambda d: d.title, reverse=True)
		elif sort_option == 'newest':
			sorted_notes = sorted(list_note, key=lambda d: d.date, reverse=True)
		return render_template('list-note.html', list_note=sorted_notes, authorized=current_user.is_authenticated)

