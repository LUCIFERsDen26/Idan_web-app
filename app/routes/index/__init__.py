from flask import Blueprint
from .resource.index import index_bp


auth_bp = Blueprint('index_bp', __name__, url_prefix='/')

# Register the login and callback blueprints with the auth blueprint
auth_bp.register_blueprint(index_bp)
