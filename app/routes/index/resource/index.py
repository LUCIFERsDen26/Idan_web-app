# auth/login.py
from flask import Blueprint, render_template, current_app


index_bp = Blueprint('index_bp', __name__)

@index_bp.route('/')
def index():
    session = current_app.config['SESSION_REDIS']
    if 'access_token' in session:
        return render_template('index.html',show=True)    
    return render_template('index.html', show= False)

@index_bp.route('/insession')
def chekcsession():
    session = current_app.config['SESSION_REDIS']
    for key in session.keys():
            print(f"key: {key} ,value: {session[key]}\n")    
    return render_template('index.html')
