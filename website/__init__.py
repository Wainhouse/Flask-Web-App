from flask import Flask
    
# a function to create the app, passes a secret to keep cookies secure
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '92466429lwkhartoum'
    
    from .views import views
    from .auth import auth

# register the url of each file
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app