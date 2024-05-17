from flask_restful import Resource
from .auth import AuthBase
from flask import redirect, current_app
from .utils import Utils
class Login(Resource,AuthBase):
    def get(self):
        auth = current_app.auth_base
        code_verifier = Utils.generate_code_verifier(48)
        uri, state = auth.client.create_authorization_url(self.authorization_endpoint, code_verifier=code_verifier,redirect_uri=self.redirect_uri)
        return redirect(uri)
