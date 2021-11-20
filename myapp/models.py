from myapp import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin
from myapp import login

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    description = db.Column(db.String(500))
    content = db.Column(db.String(5000))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password  = db.Column(db.String(128))
    # posts = db.relationship('Post', backref='author', lazy='dynamic') Spartak will look over this

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.id}: {self.username}>'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
