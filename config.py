# config.py
import os
from dotenv import load_dotenv
import logging

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SECRET_KEY = "mrfrIMEngCl0pAKqWIIBS_g"
    #SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = '1'
    REQUEST_SESSION = False
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.yml'  # Path to API specification
    APP_NAME = "IdanMotor"
    logging.basicConfig(level=logging.INFO)

class ProductionConfig(Config):
    ENV = "production"
    DEBUG = '0'
    REQUEST_SESSION = True
