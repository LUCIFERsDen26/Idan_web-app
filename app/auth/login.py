from flask_restful import Resource

from flask import redirect, current_app
from .utils import Utils
class Login(Resource):
    def get(self):
        auth = current_app.auth_base
        uri = auth.CasdoorSdk.get_auth_link(scope=auth.scope,redirect_uri=auth.redirect_uri)
        print("\nURI : ",uri)
        return redirect(uri)
