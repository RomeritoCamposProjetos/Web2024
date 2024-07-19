from flask import Flask, render_template, request, redirect, url_for

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formularios')
def formularios():
    return render_template('formulario.html')

@app.route('/form1', methods=['POST', 'GET'])
def form1():
    if request.method == 'POST':
        name = request.form['name']    
        return "Você enviou o nome: " + name
    else:
        return redirect(url_for('formularios'))
    
    
@app.route('/form2', methods=['GET', 'POST'])
def form2():
    data = request.args.get('opcao')
    return data
    