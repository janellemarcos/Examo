# class RegisterForm

    class RegisterForm(FlaskForm):
    	"""A class to represent a form for registering a new user.
    	...
    	Attributes
    	----------
    	username : str
    		submit field for username of new user
    	password : str
    		submit field for password
    	repeatPassword : str
    		submit field for same password for verification
    	submit :
    		submit the form
    	"""
    	
        username = StringField('Username', validators=[DataRequired()])
        password = PasswordField('Password', validators=[DataRequired()])
        repeatPassword = PasswordField('Repeat Password', validators=[DataRequired()])
        submit = SubmitField('Register')
