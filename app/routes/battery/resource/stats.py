from flask import Blueprint, current_app, jsonify
from ..utils import get_battery_stats
import logging

stats_bp = Blueprint('stats_bp', __name__)

@stats_bp.route('/stats')
def battery_stats():
    try:
        session = current_app.config['SESSION_REDIS']
        # Get access token and bike ID from request
        access_token = session['access_token']       
        response = get_battery_stats(access_token)
        if response:
            return jsonify(response)
        else:
            return jsonify({"error": "Invalid battery ID"})
        
    except Exception as e:
        logging.error(f"Error in get_battery_stats: {str(e)}")
        return jsonify({"error": str(e)})
