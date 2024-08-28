from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'romerito'
app.config['MYSQL_DB'] = 'avaliacao1'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

conexao = MySQL(app)

@app.route('/')
def index():
    return render_template('pages/index.html')


@app.route('/create', methods=['GET','POST'])
def create_user():
    if request.method == 'POST':
        nome = request.form['nome']
        conn = conexao.connection.cursor()
        conn.execute ("INSERT INTO users(nome) VALUES(%s)", (nome,))
        conexao.connection.commit()
        
        return redirect(url_for('index'))

    return render_template('pages/create-user.html')