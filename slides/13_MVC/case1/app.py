from flask import Flask, render_template, url_for, redirect, request, flash
import sqlite3

app = Flask(__name__)

DATABASE = 'database/database.db'
def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_connection()    
    users = conn.execute("SELECT * FROM users").fetchall()
    return render_template('index.html', users = users)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        nome= request.form['nome']

        if not email:
            flash('Email é obrigatório')
        else:
            conn = get_connection()
            conn.execute("INSERT INTO users(email, nome) VALUES (?,?)", (email, nome))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    
    return render_template('register.html')

