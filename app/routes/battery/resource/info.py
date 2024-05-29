from flask import Blueprint, current_app, jsonify
from ..utils import get_battery_info
import logging

info_bp = Blueprint('info_bp', __name__)

@info_bp.route('/info')
def battery_info():
    try:
        session = current_app.config['SESSION_REDIS']
        # Get access token and bike ID from request
        access_token = session['access_token']       
        response = get_battery_info(access_token)
        if response:
            return jsonify(response)
        else:
            return jsonify({"error": "Invalid battery ID"})
        
    except Exception as e:
        logging.error(f"Error in get_battery_info: {str(e)}")
        return jsonify({"error": str(e)})
