# def home

    @myapp_obj.route("/")
    def home():
    	"""
    	Brings the user to the homepage
    		Parameters:
    			None
    		Returns:
    			render_template (method): filled template of home.html with required variables
    	"""
    	
        if current_user.is_authenticated:
             name = current_user.username
             workMinutes = current_user.online + (datetime.utcnow() - current_user.lastOnline)
             return render_template('home.html',
             						workMinutes=workMinutes.minute, 
             						authorized=current_user.is_authenticated,
             						name=name)
    
        return render_template('home.html', authorized=current_user.is_authenticated)
