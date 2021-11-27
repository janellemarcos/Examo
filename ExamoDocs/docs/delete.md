# def delete   
    @myapp_obj.route("/delete")
    @login_required
    def delete():
        """
        Deletes the current logged in user and updates the database.
            Parameters:
                None
            Returns:
                redirect (method): redirect user to the home page.
        """
        current_id = current_user.id
        logout_user()
        User.query.filter_by(id = current_id).delete()
        db.session.commit()
        return redirect('/')