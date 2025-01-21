from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from dotenv import load_dotenv
from faker import Faker
import os

## carregar variáveis de ambiente
load_dotenv()

# objeto para criar dados fake
faker = Faker()

# fabricando conexão
engine = create_engine(os.getenv('SQLITE'))

# Definindo um objeto sessão do 'ORM' que utiliza a conexão de 'engine'
# a sessão vai usar a conexão presente em 'engine' internamente.
session = Session(bind=engine)

# Criar o banco de dados
users_table = text("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT NOT NULL
)""")

# executar declaração de criação da tabela users
session.execute(users_table)

# SQL para inserção de usuários
insert = text("""INSERT INTO users(nome) VALUES(:nome)""")

# inserindo 10 usuários no banco
for x in range(10):
    nome = faker.name()
    session.execute(insert,{'nome': nome})
    
# realizar commit após as operações de inserção
session.commit()

