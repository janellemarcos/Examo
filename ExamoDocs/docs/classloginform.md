# class LoginForm

    class LoginForm(FlaskForm):
    	"""A class to represent a filled out login form.
    	...
    	Attributes
    	----------
    	username : str
    		submitted username
    	password : str
    		submitted password
    	remember_me : bool
    		selected if user wants to be remembered
    	submit :
    		submit the form
    	"""
    	
        username = StringField('Username', validators=[DataRequired()])
        password = PasswordField('Password')
        remember_me = BooleanField('Remember me')
        submit = SubmitField('Sign in')
