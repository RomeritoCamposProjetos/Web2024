from flask import Flask, request, session, url_for, render_template, redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = '123123123'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mensagem')
def mensagem():
    return render_template('mensagem.html')

@app.route('/mural', methods=['GET', 'POST'])
def mural():
    # acesso via get tenta recurperar dados da sessão
    if request.method == 'GET':
        if 'name' in request.args:
            name = request.args.get('name')
        elif 'user' in session:
            name = session['user'] 
            
        lista = []
        if name in session.keys():
            lista = session[name]    
        return render_template('mural.html', lista=lista)
    else:
        # cada request traz um name e uma mensagem
        name = request.form['name']
        message = request.form['message']

        # o último nome enviado passa a ser o user 'logado'
        session['user'] = name

        # checagem de mensagems de usuários
        # se já possui, faz append
        if name in session.keys():
            session[name].append(message)
        else:
            session[name] = [message]
        
        return render_template('mural.html', lista=session[name])