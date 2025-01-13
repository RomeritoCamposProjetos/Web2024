from flask import Flask, render_template, request
from database import db
from database.models import *
from database.utils import start_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projeto.db'

# necessário registrar no sqlalchemy
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    size = db.session.execute(db.select(User)).scalar()
    if size == None:
        start_db()    
    return "Usuários adicionados ao banco"


@app.route('/listar')
def listar():    
    users = db.session.execute(db.select(User)).scalars()
    return render_template('listar.html', users = users)


@app.route('/listar_subs')
def listar_subs():
    nome = request.args.get('nome')
    users = []
    if nome:
        users = db.session.execute(db.select(User).where(User.name.contains(nome))).scalars()
    return render_template('listar.html', users = users)