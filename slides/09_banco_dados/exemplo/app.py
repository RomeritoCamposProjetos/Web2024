from flask import Flask, request, render_template, \
    redirect, url_for, flash
import sqlite3, os.path

DATABASE = 'database.db'

app = Flask(__name__)

# habilitar mensagens flash
app.config['SECRET_KEY'] = 'muitodificil'

# obtém conexão com o banco de dados
def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_connection()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return render_template('pages/index.html', users=users)

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        email = request.form['email']
        senha= request.form['password']

        if not email:
            flash('Email é obrigatório')
        else:
            conn = get_connection()
            conn.execute("INSERT INTO users(email, senha) VALUES (?,?)", (email, senha))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    
    return render_template('pages/create.html')