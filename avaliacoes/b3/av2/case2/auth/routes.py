from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from core.models import User

from database import session

auth_bp = Blueprint('auth', 'auth', template_folder='templates')

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('core.users'))

    if request.method == 'POST':

        nome = request.form['nome']
        senha = request.form['senha']
        usuario = session.query(User).where(User.nome == nome, User.senha == senha).first()
        if usuario:
            login_user(usuario)
            return redirect(url_for('core.users'))
        else:
            flash('*Senha ou Usuário incorreto')
        
    return render_template('login.html')

@auth_bp.route('/register', methods=['POST', 'GET'])
def register():

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        user = User(nome=nome, email=email, senha=senha)
        equal = session.query(User).where(
            User.nome == nome, 
            User.email == email).count()
        
        if not equal:
            session.add(user)
            session.commit()
            login_user(user)
            return redirect(url_for('auth.login'))
        else:
            flash('*Usuário já cadastrado')

    return render_template('register.html')


@auth_bp.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.index'))