from flask import Flask, render_template, make_response, request, redirect

app = Flask(__name__)

mensagens = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mensagem')
def mensagem():
    return render_template('mensagem.html')


@app.route('/mural', methods=['POST', 'GET'])
def mural():
    if request.method == 'GET':
        name = request.args.get('name')
        lista = []
        if name and name in mensagens.keys():
            lista = mensagens[name]
        return render_template('mural.html', lista=lista)
    else:
        # obter nome
        name = request.form['name']
        # obter mensagem
        message = request.form['message']
        # verificar se existe 
        if name in mensagens:
            mensagens[name].append(message) 
        else:
            mensagens[name] = [message]
        #cookie existe e esta ativo
        if 'name' in request.cookies and request.cookies['name'] == name:
            return render_template('mural.html', lista = mensagens[name])
        else:
            response = make_response(render_template('mural.html', lista = mensagens[name]))
            response.set_cookie(key='name', value=name)
            return response
        
