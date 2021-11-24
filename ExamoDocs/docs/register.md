# def register    
    @myapp_obj.route("/register", methods=['GET', 'POST'])
    def register():
        """
        Registers a new user and adds them to the database. If unsuccessful, prompt user to register again.
            Parameters:
                None
            Returns:
                redirect (method): redirects user to the home page on success.
        """
        form = RegisterForm()
        if form.validate_on_submit():
            if form.password.data != form.repeatPassword.data:
                flash('Repeated password is wrong')
                return redirect('register')

            try:
                p = User(username=form.username.data)
                p.set_password(password=form.password.data)
                p.lastOnline = datetime.utcnow()
                db.session.add(p)
                db.session.commit()
                login_user(p, remember=False)
                return redirect('/')
            except IntegrityError:
                flash('Username exists')
                return redirect('register')