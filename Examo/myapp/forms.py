from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password')
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')

class NoteForm(FlaskForm):
    title = StringField('title', validators=[InputRequired()])
    description = StringField('description', validators=[InputRequired()])
    content = TextAreaField('content', validators=[InputRequired()])
    submit = SubmitField('add note')


