# auth/__init__.py

from flask import Blueprint

from .resource.stats import stats_bp
from .resource.control import control_bp
from .resource.info import info_bp

battery_bp = Blueprint('battery_bp', __name__, url_prefix='/battery')

# Register the login and callback blueprints with the auth blueprint
battery_bp.register_blueprint(stats_bp)
battery_bp.register_blueprint(control_bp)
battery_bp.register_blueprint(info_bp)


