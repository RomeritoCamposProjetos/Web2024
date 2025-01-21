from flask import Blueprint, render_template
from flask_login import login_required

core = Blueprint('core', 'core', template_folder='templates')

@core.route('/')
def index():
    return render_template('index.html')

@core.route('/users')
@login_required
def users():
    return render_template('core/users.html')
