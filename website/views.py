from flask import Blueprint, render_template
from flask_login import  login_required, current_user


# the blueprint for this page
views = Blueprint('views', __name__)

# Create the url route
@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)