from flask import Blueprint, render_template

# the blueprint for this page
views = Blueprint('views', __name__)

# Create the url route
@views.route('/')
def home():
    return render_template("home.html")