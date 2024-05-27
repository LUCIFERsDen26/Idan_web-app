# auth/logout.py
from flask import Blueprint, current_app, jsonify, redirect, flash

from ..utils import Utils
import logging

logout_bp = Blueprint('logout_bp', __name__)

@logout_bp.route('/logout')
def logout():

    # Get the authorization code and state from the request
    session = current_app.config['SESSION_REDIS']
    
    
    if 'access_token' not in session:
        logging.error('user not logged in yet.')
        flash('please login first')
        return redirect('/')

    logging.info('user has toekn in session')
    
    try:
        logging.info('Tring to logout user ')
        status = Utils.logout_from_casdoor(access_token=session['access_token'])       
        if status:
            del session
            logging.info('user has been logged out successfully')
            flash('You were successfully logged out')
            return redirect('/'), 301       

    except Exception as e:
        logging.info('user has not been logged out successfully')
        logging.error('Error while processing callback: %s', e)
        return jsonify({'error': 'An error occurred while processing the callback'}), 500

    return {'error': 'An error occurred while processing the callback'}, 500

"""
curl -X GET   http://0.0.0.0:8000/api/logout   -H "Authorization: Bearer eyJhbGciOiJSUzI1
"""
