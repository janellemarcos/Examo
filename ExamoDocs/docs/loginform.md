# class LoginForm

    class LoginForm(FlaskForm):
    	"""A class to represent a form for logging into the website.
    	...
    	Attributes
    	----------
    	username : str
    		submit field for username
    	password : str
    		submit field for password
    	remember_me : bool
    		selected if user wants to be remembered
    	submit :
    		submit the form
    	"""
    	
        username = StringField('Username', validators=[DataRequired()])
        password = PasswordField('Password')
        remember_me = BooleanField('Remember me')
        submit = SubmitField('Sign in')
