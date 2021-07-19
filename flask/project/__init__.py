from flask import Flask, logging as flask_logging
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from project import routes
import os
import logging
SECRET_KEY = os.urandom(32)

def create_app(config):
    """
    The application factory. Returns an instance of the app.
    """
    csrf = CSRFProtect()
    # create the application object
    app = Flask(__name__)
    register_blueprints(app)
    config_logger(app)

    app.config['SECRET_KEY'] = SECRET_KEY

    # todo - separate out and register?
    Bootstrap(app)
    # csrf.init_app(app)
    
    return app

def register_blueprints(app):
    app.register_blueprint(routes.routes)


def config_logger(app):
    logging.basicConfig(
        format="[%(levelname)s] %(asctime)s %(name)s (%(funcName)s, line %(lineno)s): %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
    )
    flask_logging.create_logger(app)
