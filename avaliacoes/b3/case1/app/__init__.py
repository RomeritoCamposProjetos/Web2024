from flask import Flask, render_template
from users import users
from books import books

# importar auth_bluprint e login_manager (PROVA)
from auth.bp import auth_bp, login_manager

app = Flask (__name__, template_folder='templates')

# secret key (PROVA)
app.config['SECRET_KEY'] = 'SENHASENHASENHA'

#Inicializar app no login_manage (prova)
login_manager.init_app(app)

# registrar blueprint
app.register_blueprint(auth_bp)

app.register_blueprint(users.bp)
app.register_blueprint(books.bp)


@app.route('/')
def index():
    return render_template('layout.html')