from flask import Blueprint, render_template
from flask_login import login_required
from database import session
from core.models import User

core = Blueprint('core', 'core', template_folder='templates')

@core.route('/')
def index():
    return render_template('index.html')

@core.route('/users')
@login_required
def users():

    users = session.query(User).all()

    return render_template('core/users.html', lista_users=users)

# @core.route('/dashboard')
# @login_required
# def dash():
#     return render_template('core/index.html')