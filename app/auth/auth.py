# auth/auth.py

from authlib.integrations.requests_client import OAuth2Session
import requests
import os 
from .utils import Utils
from flask import current_app   

class AuthBase:
    def __init__(self):
        self.client_id = os.environ['CLIENT_ID']
        if current_app:
            session = requests.Session()
            session.verify = current_app.config['REQUEST_SESSION']
        self.verify = os.environ.get('CURL_CA_BUNDLE','')
        
        openID = Utils.fetch_url_data("https://host.docker.internal:9443/oauth2/token/.well-known/openid-configuration")

        self.signing_algos = openID["id_token_signing_alg_values_supported"]
        self.authorization_endpoint = openID['authorization_endpoint']
        self.token_endpoint = openID['token_endpoint']
        self.revok_endpoint = openID['revocation_endpoint']
        scope = 'openid email phone'
        self.my_info_endpoint = openID['userinfo_endpoint']
        
        self.my_account  = "https://localhost:9443/t/carbon.super/myaccount/overview"


        self.redirect_uri = "http://127.0.0.1:5000/callback"
        
        self.client = OAuth2Session(self.client_id, 
                       redirect_uri=self.redirect_uri, 
                       scope=scope, 
                       code_challenge_method='S256'                       
                      )

