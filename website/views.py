from flask import Blueprint

# the blueprint for this page
views = Blueprint('views', __name__)

# Create the url route
@views.route('/')
def home():
    return "<h1>Test</h1>"