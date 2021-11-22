from myapp import myapp_obj
from myapp.forms import LoginForm
from myapp.forms import RegisterForm
from flask import render_template, flash, redirect
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime, timedelta
from myapp import db

@myapp_obj.route("/")
def home():
    if current_user.is_authenticated:
         name = current_user.username
         workMinutes = current_user.online + (datetime.utcnow() - current_user.lastOnline)
         return render_template('home.html', workMinutes=workMinutes.minute, authorized=current_user.is_authenticated, name=name)

    return render_template('home.html', authorized=current_user.is_authenticated)
