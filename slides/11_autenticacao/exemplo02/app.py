from flask import Flask, redirect, render_template, url_for, request, flash
import sqlite3
from models import User
from werkzeug.security import check_password_hash, generate_password_hash

# 1 - Adicionar o LoginManager
from flask_login import LoginManager, login_user, login_required, logout_user
login_manager = LoginManager()

app = Flask(__name__)

# 2 - Configurar app para trabalhar junto com flask-login
login_manager.init_app(app)

# 3 - ncessário adicionar uma chave secreta para aplicaçãos
app.config['SECRET_KEY'] = 'ULTRAMEGADIFICIL'

# 4-  Função utilizada para carregar o usuário da sessão (logado)
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def index():    
    return render_template('index.html',users = User.all())

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']        
        if not User.exists(email):
            user = User(email=email, password=password)
            user.save()            
            # 6 - logar o usuário após cadatro
            login_user(user)
            flash("Cadastro realizado com sucesso")
            return redirect(url_for('dash'))
    return render_template('pages/auth/register.html')


# 7 - logar um usuário já existente
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']   
        user = User.get_by_email(email)
        if check_password_hash(user['password'], password):
            login_user(User.get(user['id']))
            flash("Você está logado")
            return redirect(url_for('dash'))
        else:
            flash("Dados incorretos")
            return redirect(url_for('login'))
    return render_template('pages/auth/login.html')
             
# 5 - bloquear uma rota
@app.route('/dashboard')
@login_required
def dash():
    return render_template('pages/dash.html')

# 8 - logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
