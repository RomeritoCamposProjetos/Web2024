from flask import render_template, Blueprint, url_for, request, flash, redirect
from users.models import User
from flask_login import login_required

# módulo de usuários
bp = Blueprint('users', __name__, url_prefix='/users', template_folder='templates')

@bp.route('/')
@login_required
def index():
    return render_template('users/index.html', users = User.all())

@bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        nome= request.form['nome']

        if not email:
            flash('Email é obrigatório')
        else:
            user = User(nome=nome, email=email)
            user.save()
            return redirect(url_for('auth.login'))
    
    return render_template('users/register.html')
