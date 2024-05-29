from flask import Blueprint, current_app, jsonify, render_template, request
from ..utils import get_battery_settings, set_battery_settings
import logging

control_bp = Blueprint('control_bp', __name__)

@control_bp.route('/control')
def battery_control():
    """
    Retrieves battery information and renders the control template.

    Handles potential exceptions during session access or battery settings retrieval.
    Logs errors and returns appropriate error messages if exceptions occur.
    """

    try:
        session = current_app.config['SESSION_REDIS']

        # Get access token and bike ID from request in a more secure way
        access_token = session.get('access_token')  # Use .get() to avoid potential KeyError
        if not access_token:
            # Handle missing access token (e.g., redirect to login)
            return jsonify({"error": "Missing access token"}), 401  # Unauthorized

        param = get_battery_settings(access_token)
        print(param)
        return render_template('control.html', parms=param)

    except Exception as e:
        logging.error(f"Error retrieving battery info: {str(e)}")
        return jsonify({"error": "An error occurred while getting battery information."}), 500  # Internal Server Error

@control_bp.route('/update', methods=['POST'])
def update_battery_params():
    """
    Updates battery settings and returns a JSON response.

    Handles potential exceptions during data access, validation, or battery settings update.
    Logs errors and returns appropriate error messages if exceptions occur.
    """

    try:
        session = current_app.config['SESSION_REDIS']

        # Get access token and bike ID from request in a more secure way (same as above)
        access_token = session.get('access_token')
        if not access_token:
            return jsonify({"error": "Missing access token"}), 401  # Unauthorized

        # Get form data
        data = request.form.to_dict()

        # Perform data validation (implement validation logic here)
        # ...

        response = set_battery_settings(access_token, data)
        return response

    except Exception as e:
        logging.error(f"Error updating battery settings: {str(e)}")
        return jsonify({"error": "An error occurred while updating battery settings."}), 500  # Internal Server Error
