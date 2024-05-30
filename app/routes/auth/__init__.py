# auth/__init__.py
from casdoor import CasdoorSDK
import os
from flask import Blueprint

from .resource.login import login_bp
from .resource.callback import callback_bp
from .resource.logout import logout_bp

from .utils import Utils
auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

# Register the login and callback blueprints with the auth blueprint
auth_bp.register_blueprint(login_bp)
auth_bp.register_blueprint(callback_bp)
auth_bp.register_blueprint(logout_bp)


class CasdoorAuthBase:
    def __init__(self):

        self.client_id = os.environ['CASDOOR_CLIENT_ID']
        
        self.client_certs = str(os.environ['CASDOOR_CLIENT_CERTS'])
                                
        openID = Utils.fetch_url_data(os.environ['CASDOOR_OPENID_CONFIG_URL'])
        
        self.signing_algos = openID["id_token_signing_alg_values_supported"]
        self.authorization_endpoint = openID['authorization_endpoint']
        self.token_endpoint = openID['token_endpoint'].replace("https", "http")
        self.end_session_endpoint = openID['end_session_endpoint'].replace("https", "http")
        self.scope = 'openid email phone phone'

        self.redirect_uri = "http://127.0.0.1:5000/callback"

        self.sdk = CasdoorSDK(
                            endpoint=openID['issuer'],
                            client_id=self.client_id,
                            certificate=self.client_certs,
                            client_secret=None,
                            org_name=os.environ['CASDOOR_ORG_NAME'],
                            application_name=os.environ['CASDOOR_APPLICATION_NAME'],
                            front_endpoint=os.environ['CASDOOR_FRONT_ENDPOINT'],
                      )
