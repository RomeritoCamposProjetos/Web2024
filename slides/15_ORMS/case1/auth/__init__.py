from flask_login import LoginManager, login_user
from flask import Blueprint, render_template, request,url_for, redirect, flash
from models import User
from database import db
from werkzeug.security import check_password_hash

auth_bp = Blueprint(name="auth", 
    import_name=__name__, 
    url_prefix='/auth',
    template_folder='templates')

login_manager = LoginManager()

@login_manager.user_loader
def load_user():
    pass

@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        user = User(nome, email, senha)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        user = db.session.execute(db.select(User).where(User.email == email))
        print(user)
        if check_password_hash(user.senha, senha):            
            login_user(user)
        else:
            flush('Erro nos dados')       
        
        
    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    pass