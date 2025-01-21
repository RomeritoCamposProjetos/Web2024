from sqlalchemy import create_engine
from sqlalchemy.sql import text
from dotenv import load_dotenv
from faker import Faker
from os import getenv

# carregar os dados de ambiente .env
load_dotenv()

# criar dados fictíceis 
faker = Faker()

# fabrica de conexões  
engine = create_engine(getenv('SQLITE'))

# a função text() é usada para criar objetos com sql executáveis
users_table = text("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT NOT NULL
)""")

# retorna um objeto Connection, permitindo execução de instruções SQL
connection = engine.connect()

# executa a criaçaõ de uma tabela
connection.execute(users_table)

# SQL para inserção de usuários
insert = text("""INSERT INTO users(nome) VALUES(:nome)""")

# inserindo 10 usuários no banco
for x in range(10):
    nome = faker.name()
    connection.execute(insert,{'nome': nome})
    
# realizar commit após as operações de inserção
connection.commit()