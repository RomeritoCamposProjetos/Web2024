from flask import Flask, render_template, request

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/register', methods= ['POST', 'GET'])
def register():
    nome = request.form.get('nome')
    if request.method == 'POST':
        return "<h1> Oi, {}!".format(nome)
    elif request.method == 'GET':
        data='Method Not Allowed'
        return render_template('error.html', data=data), 405

@app.route('/listar')
def listar():
    filter = request.args.get('filter')
    
    listas = {
        'books' : ['Python', 'Flask', 'Web dev', 'Python Cookbook'],
        'sports' : ['Running', 'Soccer', 'Voleyball', 'Basketball'],
    }
    
    if filter in listas:
        return render_template('produtos.html',data=listas[filter])
    else:
        # return Bad Request
        data = 'Bad Request'
        return render_template('error.html', data), 400
