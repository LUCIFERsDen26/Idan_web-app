# auth/callback.py
from flask import Blueprint, request, current_app, jsonify, redirect

from ..utils import Utils
import logging

callback_bp = Blueprint('callback_bp', __name__)

@callback_bp.route('/callback')
def callback():

    # Get the authorization code and state from the request
    session = current_app.config['SESSION_REDIS']
    auth = current_app.auth_base
    code = request.args.get('code', None)
    state = request.args.get('state', None)

    if not code:
        logging.error('No authorization code provided.')
        return jsonify({'error': 'Authorization code not found'}), 400

    logging.info('Authorization code received: %s', code)
    
    try:
        
        payload = Utils.generate_payload(code_value=code, verifier=session['code_verifier'])
        tokens = auth.sdk._oauth_token_request(payload).json()
        
        logging.info('Tokens generated successfully: ')
        session['access_token'] = tokens['access_token']
        session['refresh_token'] = tokens['refresh_token']
        session['id_token'] = tokens['id_token']
        return redirect('/')

    except Exception as e:
        logging.error('Error while processing callback: %s', e)
        return jsonify({'error': 'An error occurred while processing the callback'}), 500
