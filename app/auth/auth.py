# auth/auth.py

from casdoor import CasdoorSDK
import requests
import os 
from .utils import Utils
from flask import current_app   

class CasdoorAuthBase:
    def __init__(self):

        self.client_id = os.environ['CLIENT_ID']
        self.client_certs = os.environ['CLIENT_CERTS']

        if current_app:
            session = requests.Session()
            session.verify = current_app.config['REQUEST_SESSION']
        self.verify = os.environ.get('CURL_CA_BUNDLE','')
                                       
        openID = Utils.fetch_url_data("http://host.docker.internal:8000/.well-known/openid-configuration")

        self.signing_algos = openID["id_token_signing_alg_values_supported"]
        self.authorization_endpoint = openID['authorization_endpoint']
        self.token_endpoint = openID['token_endpoint']
        
        self.scope = 'openid email phone'
        self.my_info_endpoint = openID['userinfo_endpoint']

        self.redirect_uri = "http://127.0.0.1:5000/callback"
        
        self.CasdoorSdk = CasdoorSDK(
                            endpoint=openID['issuer'],
                            client_id=self.client_id,
                            certificate=self.client_certs,
                            org_name="IdanMotor",
                            application_name="Idan_FrontEnd",                                                 
                            client_secret=None                     
                      )

