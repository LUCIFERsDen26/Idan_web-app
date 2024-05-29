# app/__init__.py

# Import necessary modules
import os
from redis import Redis
from flask import Flask
from flask_session import Session


# Import blueprints
from .routes.auth import auth_bp, CasdoorAuthBase
from .routes.index import index_bp
from .routes.battery import battery_bp

def create_app():
    """
    Create and configure the Flask application.

    Returns:
        Flask: The Flask application.
    """
    # Create the Flask application
    app = Flask(__name__)

    # Set the secret key for the application
    app.secret_key = app.config['SECRET_KEY']

    # Load the configuration from the environment
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)
    os.environ['FLASK_DEBUG'] = app.config['DEBUG']

    # Create and initialize the Flask-Session object AFTER `app` has been configured
    server_session = Session(app)

    # Create an instance of the CasdoorAuthBase class and attach it to the application context
    with app.app_context():
        app.auth_base = CasdoorAuthBase()

    # Register the blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(battery_bp)
    # Return the Flask application
    return app