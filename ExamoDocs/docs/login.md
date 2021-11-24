# def login

    @myapp_obj.route("/login", methods=['GET', 'POST'])
    def login():
        """
        Logs the user in on success, otherwise prompt user to enter their credentials again.
            Parameters:
                None
            Returns:
                render_template (method): the login.html form that the user will fill out.
        """
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Login invalid username or password!')
                return redirect('/login')

            login_user(user, remember=form.remember_me.data)
            flash(f'Login requested for user {form.username.data}')
            flash(f'Login password {form.password.data}')

            #Check if 24 hours passed and reset online timer
            if(datetime.utcnow() - current_user.lastOnline) > timedelta(1):
                current_user.online = datetime(1,1,1,0,0)
            current_user.lastOnline = datetime.utcnow()
            db.session.commit()
            return redirect('/')
        return render_template("login.html", form=form, authorized=current_user.is_authenticated)