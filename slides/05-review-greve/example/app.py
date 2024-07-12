# instalar o flask
from flask import Flask, render_template, request

# criando uma aplicação
app = Flask(__name__)

# definindo uma rota
@app.route('/')
def index():
    return "Hello World"

# usando template
@app.route('/formulario', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
        return render_template('formulario.html')
    else:
        name = request.form['name']
        return name

# rota dinâmica com string de consulta
@app.route('/rota-dinamica/<nome>')
def rota_dinamica(nome):
    return render_template('rota_dinamica.html', dado=nome)

# maneira de executar
# if __name__ == '__main__':
#     app.run(host='127.0.0.1', debug=True)