from flask import Blueprint, current_app, render_template, flash
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
        print("no error")
        if response:
            return render_template('batterypages/stats.html', data=response)
        else:
            flash( "Invalid battery ID")
            return "<p>Invalid battery ID</p>"
        
    except Exception as e:
        logging.error(f"Error in get_battery_stats: {str(e)}")
        flash("error")
        return "<p>error</p>"
