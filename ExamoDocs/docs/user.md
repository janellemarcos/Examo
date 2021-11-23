# class User

    class User(UserMixin, db.Model):
    	"""A class to represent a user.
    	...
    	Attributes
    	----------
    	id : int
    		reference id
    	username : str
    		username of the user
    	password : str
    		password of the user
    	online : time
    		time stamp stating user is online
    	lastOnline : time
    		time stamp stating when user was last online
    	notes : obj
    		all notes associated with user
    	"""
    	
        __tablename__ = 'User'
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(64), unique=True, index=True)
        password  = db.Column(db.String(128))
        online = db.Column(db.DateTime, default=datetime(1,1,1,0,0))
        lastOnline = db.Column(db.DateTime, default=datetime.utcnow())
        notes = db.relationship('Note', secondary=UserNote, backref='Author')
    
        def set_password(self, password):
        	"""
        	Set password
        		Parameters:
        			self (ref): reference to current instance of user
        			password (str): password to be set for current user
        		Returns: 
        			None
        	"""
            self.password = generate_password_hash(password)
    
        def check_password(self, password):
            """
        	Check password
        		Parameters:
        			self (ref): reference to current instance of user
        			password (str): password of current user
        		Returns:
        			check_password_hash (bool): true if instance password matches current user's database password
        	"""
            return check_password_hash(self.password, password)
    
        def __repr__(self):
            """
        	Constructs
        		Parameters:
        			self (ref): reference to current instance of user
        		Returns:
        			printable representation of self
        	"""
            return f'<User {self.id}: {self.username}>'
