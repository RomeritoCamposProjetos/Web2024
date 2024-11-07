from flask import Flask
from controllers import users, books

# importar o bluprint e o login manager
from auth.bp import auth_bp, login_manager

app = Flask(__name__)

# configurar secret key
app.config['SECRET_KEY'] = 'dificil'
# inicializar o app no login manager
login_manager.init_app(app)
# registrando o blueprint
app.register_blueprint(auth_bp)

app.register_blueprint(users.bp)
app.register_blueprint(books.bp)

@app.route('/')
def index():
    return "<h1>Teste</h1>"