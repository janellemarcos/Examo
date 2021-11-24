# class ShareForm

    class ShareForm(FlaskForm):
    	"""A class to represent a form for sharing a note.
    	...
    	Attributes
    	----------
    	username : str
    		submit field for username to share the note with
    	submit :
    		submit the form
    	"""
    	
        username = StringField('Username', validators=[DataRequired()])
        submit = SubmitField('Share')
