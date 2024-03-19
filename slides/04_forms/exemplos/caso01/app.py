from flask import Flask, request, render_template, abort
from faker import Faker

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        if email == 'admin@email.com' and senha == '123123':
            return render_template('dashboard.html')
        else:
            return render_template('errors/401.html'), 401

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/buscar')
def search():
    lista = ['livro', 'pc', 'camisa', 'relogio']
    item = request.args.get('item')
    resultado = {}
    #obter string de consulta
    if item in lista:
        faker = Faker(locale="pt_BR")
        for x in lista:
            resultado[x] = [ faker.job() for y in range(50) ]
        return render_template('produtos.html', produtos=resultado[item])
    else:
        return render_template('errors/400.html'), 400
        

    