from myapp import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin
from myapp import login
from datetime import datetime, timedelta

#One to many relationship between User and Note
UserNote = db.Table('UserNote',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('User.id')),
    db.Column('note_id', db.Integer, db.ForeignKey('Note.id')))

class Note(db.Model):
    __tablename__ = 'Note'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    description = db.Column(db.String(500))
    content = db.Column(db.String(5000))
    users = db.relationship('User', secondary=UserNote, backref='Note')

class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password  = db.Column(db.String(128))
    online = db.Column(db.DateTime, default=datetime(1,1,1,0,0))
    lastOnline = db.Column(db.DateTime, default=datetime.utcnow())
    notes = db.relationship('Note', secondary=UserNote, backref='Author')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.id}: {self.username}>'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
