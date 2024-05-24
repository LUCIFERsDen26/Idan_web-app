# app/__init__.py

import os
from flask import Flask

# Import and register the auth blueprint
from .auth import auth_bp, CasdoorAuthBase
from .index import index_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'my_secret_key'

    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)
    os.environ['FLASK_DEBUG'] =  app.config['DEBUG']

    # Create an instance of the CasdoorAuthBase class and attach it to the application context
    with app.app_context():
        app.auth_base = CasdoorAuthBase()

    # Register the auth blueprint with the Flask app
    app.register_blueprint(auth_bp)

    # Register the index blueprint with the Flask app
    app.register_blueprint(index_bp)

    return app
