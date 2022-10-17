from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

# each page/url this app will use
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
            else:
                flash('Incorrect password, try again.', category='error')
        else:
                flash('Email does not exist.', category='error')

    return render_template("login.html", boolean = True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
       email = request.form.get('email')
       firstName = request.form.get('firstName')
       pasword1 = request.form.get('password1')
       password2 = request.form.get('password2')

       user = User.query.filter_by(email=email).first()
       if user:
            flash('Email already exists.', category='error')
       elif len(email) < 6:
            flash('Email must be greater than 4 characters.', category='error')
       elif len(firstName) < 2:
            flash('Firstname must be greater than 2 characters.', category='error')
       elif pasword1 != password2:
            flash('Passwords don\'t match.', category='error')
       elif len(pasword1) < 7:
            flash('Password too short, must be 7 characters.', category='error')
       else:
            new_user = User(email=email, first_name=firstName, password= generate_password_hash(pasword1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()   
            flash('Account Created.', category='success')
            return redirect(url_for('views.home'))
            

    return render_template("sign_up.html")


