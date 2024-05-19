# auth/callback.py
from flask import Blueprint, request, current_app, jsonify, session, make_response, redirect
from ..utils import Utils
import logging

callback_bp = Blueprint('callback_bp', __name__)

@callback_bp.route('/callback')
def callback():
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
        
        del session['code_verifier']
        # Set the access token as an HTTP-only cookie
        response = make_response(redirect('/'))
        response.set_cookie('access_token', tokens['access_token'], httponly=True)
        response.set_cookie('refresh_token', tokens['refresh_token'], httponly=True)
        response.set_cookie('id_token', tokens['id_token'], httponly=True)
        return response

    except Exception as e:
        logging.error('Error while processing callback: %s', e)
        return jsonify({'error': 'An error occurred while processing the callback'}), 500
