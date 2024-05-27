# auth/login.py
from flask import Blueprint, redirect, current_app
from ..utils import Utils

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login')
def login():
    session = current_app.config['SESSION_REDIS']
    
    code_verifier, code_challenge = Utils.generate_code_verifier_and_code_challenge()
    uri = Utils.generate_auth_uri(code_challenge)
    
    
    session['code_verifier'] = code_verifier
    session['code_challenge'] = code_challenge

    for key in session.keys():
        print(f"key: {key} ,value: {session[key]}\n")
    return redirect(uri)

