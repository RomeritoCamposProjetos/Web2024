from flask import Flask, render_template
from controllers.users import users_bp
from auth import auth_bp, login_manager
from database import db

app = Flask(__name__)
app.config['SECRETE_KEY'] = 'dificil'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'

# Inicializações
db.init_app(app)
login_manager.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)

# criação das tabelas
with app.app_context():
    db.create_all()

#rota inicial
@app.route('/')
def index():
    return render_template('index.html')