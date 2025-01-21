from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, login_user, logout_user
from core.models import User

auth_bp = Blueprint('auth', 'auth', template_folder='templates')

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        # fazer a busca no banco pelo usuário pelo nome
        # Aqui você precisa de fato pegar o usuário no banco e logar ele
        usuario = User()
        usuario.id = 1

        if usuario:
            login_user(usuario)
            return redirect(url_for('core.users'))
        
    return render_template('login.html')

@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
    return render_template('register.html')


@auth_bp.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.index'))