# auth/__init__.py

from flask import Blueprint

from .resource.stats import stats_bp
from .resource.control import control_bp
from .resource.info import info_bp


from .utils import Utils
bike_bp = Blueprint('bike_bp', __name__, url_prefix='/bike')

# Register the login and callback blueprints with the auth blueprint
bike_bp.register_blueprint(stats_bp)
bike_bp.register_blueprint(control_bp)
bike_bp.register_blueprint(info_bp)


