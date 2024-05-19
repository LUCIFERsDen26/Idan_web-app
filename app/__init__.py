# app/__init__.py

import os
from flask import Flask, session, current_app
from flask_swagger_ui import get_swaggerui_blueprint
# Import and register the auth blueprint
from .auth import auth_bp, CasdoorAuthBase

def create_app():
    app = Flask(__name__)
    app.secret_key = 'my_secret_key'

    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)
    os.environ['FLASK_DEBUG'] =  app.config['DEBUG']

    # Conditionally register Swagger UI if the environment is set to development
    if app.config['ENV'] == "development":

        # Retrieve Swagger configuration from DevelopmentConfig
        swagger_url = app.config['SWAGGER_URL']
        api_url = app.config['API_URL']
        app_name = app.config['APP_NAME']

        swagger_blueprint = get_swaggerui_blueprint(
            swagger_url,
            api_url,
            config={'app_name': app_name}
        )
        app.register_blueprint(swagger_blueprint, url_prefix=swagger_url)

    # Create an instance of the CasdoorAuthBase class and attach it to the application context
    with app.app_context():
        app.auth_base = CasdoorAuthBase()

    # Register the auth blueprint with the Flask app
    app.register_blueprint(auth_bp)

    return app
