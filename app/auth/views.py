
from . import auth
from flask import render_template, redirect, url_for, flash, request
from ..models import User, Pitch, Category
from flask_login import login_user, logout_user, login_required
from .forms import LoginForm, RegistrationForm
from .. import db
from ..email import mail_message
# from ..email import mail_message

'''
@auth.route('/login')
def login():
    return render_template('auth/login.html')
'''

@auth.route('/register', methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            user = User(email=form.email.data, username=form.username.data, password=form.password.data)
            db.session.add(user)
            # mail_message("Welcome to Pitches", "email/welcome_user", user.email, user=user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        except Exception: 
            db.session.rollback()
            return render_template('auth/register.html', registration_form=form)
        
    return render_template('auth/register.html', registration_form=form)

@auth.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Pitches login"
    return render_template('auth/login.html', login_form=login_form, title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route('/AddPitch', methods=["GET", "POST"])
def Addpitch():
    new_pitch = Pitch()
    new_pitch.save_pitch()
    
    title = 'Adding new pitches'
    return render_template('auth/AddPitchesForm.html', title=title)

