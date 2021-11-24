# def logout

    @myapp_obj.route("/logout")
    def logout():
        """
        Logs the current user out of their account.
            Parameters:
                None
            Returns:
                redirect (method): redirects the user to the home page.
        """
        current_user.online = current_user.online + (datetime.utcnow() - current_user.lastOnline)
        db.session.commit()
        logout_user()
        return redirect('/')