from flask import Flask
from flask_bootstrap import Bootstrap

from project import routes
import os
SECRET_KEY = os.urandom(32)

def create_app(config):
    """
    The application factory. Returns an instance of the app.
    """

    # create the application object
    app = Flask(__name__)
    register_blueprints(app)
    app.config['SECRET_KEY'] = SECRET_KEY

    # todo - separate out and register?
    Bootstrap(app)
    
    return app

def register_blueprints(app):
    app.register_blueprint(routes.routes)
