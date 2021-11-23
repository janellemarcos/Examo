# class Note

    class Note(db.Model):
    	"""A class to represent a note.
    	...
    	Attributes
    	----------
    	id : int
    		reference id
    	title : str
    		note title
    	description : str
    		a short description of the note
    	content : str
    		note content
    	users : 
    		all users associated with the note
    	"""
    	
        __tablename__ = 'Note'
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(64), index=True)
        description = db.Column(db.String(500))
        content = db.Column(db.String(5000))
        users = db.relationship('User', secondary=UserNote, backref='Note')
