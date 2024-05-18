# app/__init__.py
#import config
import os
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

# import resources
from .auth.auth import CasdoorAuthBase
from .auth.login import Login

def create_app():
    app = Flask(__name__)
    
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

    # Create the Flask-RESTful API instance
    api = Api(app)
    with app.app_context():
        # Initialize AuthBase and attach it to the application context
        app.auth_base = CasdoorAuthBase()

    # add resources
    api.add_resource(Login, '/auth/login')
    


    return app
