from flask import Flask, render_template
from flask import request


# criação de app Flask
# __name__ nome do módulo ou pacote (main.py --> __main__)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    if request.method == 'POST':
        return request.form['nome']        
    elif request.method == 'GET':
        return "Unsuported Method"
    

@app.route('/profile2', methods=['POST'])
def profile2():
    
    data = [(k, v )for k, v in request.headers.items()]
    return render_template('content-type1.html',data=data)
