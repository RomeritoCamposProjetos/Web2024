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


@app.route('/listar-usuario')
def listar():
    conn = conexao.connection.cursor()
    conn.execute('SELECT * FROM users')
    users = conn.fetchall()
    conn.close()
    return render_template('pages/listar-users.html', users = users)

@app.route('/<int:id>/listar')
def listar_user(id):
    conn = conexao.connection.cursor()
    conn.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = conn.fetchone()
    conn.close()
    if user:
        return render_template('pages/show-user.html', user=user)        
    return "Usuário não encontrado"

@app.route('/create_peca', methods=['POST', 'GET'])
def create_peca():
    if request.method == 'POST':
        titulo = request.form['titulo']
        conn = conexao.connection.cursor()
        conn.execute("INSERT INTO pecas(titulo) VALUES (%s)", (titulo,))
        conexao.connection.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('pages/create-pecas.html')
    
@app.route('/<int:id>/listar_peca')
def listar_peca(id):
    conn = conexao.connection.cursor()
    conn.execute("SELECT * FROM pecas WHERE id = %s", (id,))
    peca = conn.fetchone()
    conn.close()
    if peca:
        return render_template('pages/show-peca.html', peca=peca)
    return "Esta peça não existe";  