from flask import Flask
from controllers import users, books

# importar o bluprint e o login manager (PROVA)


app = Flask(__name__)

# configurar secret key (PROVA)

# inicializar o app no login manager (PROVA)

# registrando o blueprint (PROVA)


app.register_blueprint(users.bp)
app.register_blueprint(books.bp)

@app.route('/')
def index():
    return "<h1>Teste</h1>"