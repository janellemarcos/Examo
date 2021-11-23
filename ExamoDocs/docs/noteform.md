# class NoteForm

    class NoteForm(FlaskForm):
    	"""A class to represent a form for creating a note.
    	...
    	Attributes
    	----------
    	title : str
    		submit field for note title
    	description : str
    		submit field for a short description
    	content : str
    		submit field for note content
    	submit :
    		submit the note
    	"""
    	
        title = StringField('title', validators=[DataRequired()])
        description = StringField('description')
        content = TextAreaField('content')
        submit = SubmitField('Save')
