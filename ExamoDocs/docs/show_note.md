# def show_note

    @myapp_obj.route('/show-note/<id>', methods=['GET'])
    @login_required
    def show_note(id):
        """
        Shows the note that the user clicked on. If the note does not exist, redirect the user to the list of notes page.
            Parameters:
                id (int): the id of the note.
            Returns:
                render_template (method): shows the title, description, and content of the desired note if it exists.
        """
        note = Note.query.join(Note.users).filter(User.id==current_user.id, Note.id==id).first()
        if note == None:
            return redirect('/list-note')

        note.content = '\n'+note.content
        return render_template('show-note.html', note=note, authorized=current_user.is_authenticated)
