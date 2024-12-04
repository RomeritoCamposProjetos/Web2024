from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from faker import Faker
from dotenv import load_dotenv
import os

# classe definida em models.py - 
from models import Base, User

# carregar variáveis de ambiente
load_dotenv()

# utilizado para fabricar dados 
faker = Faker()

# criar conexão com banco
engine = create_engine(os.getenv('SQLITE'))

# A classe base utiliza os metadados dos modelos para 
# criar a estrutura no banco de dados
Base.metadata.create_all(bind=engine)

# Cria sessão para manipulação do banco
session = Session(bind=engine)

# criação e adição de 10 usuários ao banco
for x in range(10):
    user = User(nome=faker.name())
    session.add(user)
    
session.commit ()


# Porque não cria sqlite_seqeunte no banco?