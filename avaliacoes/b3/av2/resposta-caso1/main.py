from core.core import core
from auth import login_manager
from auth.routes import auth_bp
from flask import Flask
from database import Base, engine

# Inicializa a apliacação
application = Flask(__name__)
application.config['SECRET_KEY'] = '123123123123'

#criação do banco de dados
Base.metadata.create_all(bind=engine)

# Inicializa o controle de sessões
login_manager.init_app(application)

# Registra as rotas da aplicação
application.register_blueprint(core)

# Registra rotas de login/logout
application.register_blueprint(auth_bp)


