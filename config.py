# config.py
import os
from dotenv import load_dotenv
import logging

dotenv_path = os.path.join(os.path.dirname(__file__), '.appenv')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SECRET_KEY = "mrfrIMEngCl0pAKqWIIBS_g"
    #SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = '1'
    REQUEST_SESSION = False
    logging.basicConfig(level=logging.INFO)
    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    import redis
    SESSION_REDIS = redis.from_url('redis://host.docker.internal:6379')

class ProductionConfig(Config):
    ENV = "production"
    DEBUG = '0'
    REQUEST_SESSION = True
