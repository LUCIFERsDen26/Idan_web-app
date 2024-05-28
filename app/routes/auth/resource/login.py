# auth/login.py
from flask import Blueprint, redirect, current_app, flash
from ..utils import Utils
import logging
login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login')
def login():
    session = current_app.config['SESSION_REDIS']
    
    if 'access_token' in session:
        flash('you are already logged in')
        logging.info('user has toekn in session')
        return "<a href='/'>Home</a></br><p>you are already logged in</p>"
    
    else:
        logging.info('user has toekn not in session')
        code_verifier, code_challenge = Utils.generate_code_verifier_and_code_challenge()
        uri = Utils.generate_auth_uri(code_challenge)
        
        session['code_verifier'] = code_verifier
        session['code_challenge'] = code_challenge
        
        return redirect(uri)

