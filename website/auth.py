from flask import Blueprint

auth = Blueprint('auth', __name__)

# each page/url this app will use
@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>sign-up</p>"


