from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from models import User
from sqlalchemy import select, insert, delete, update
import os

# carregar as variáveis de ambiente
load_dotenv()

engine = create_engine(os.getenv('SQLITE'))
session = Session(bind=engine)


# Referenência para operadores
# https://docs.sqlalchemy.org/en/20/core/operators.html

print("\n------------------- select 1 -----------------------")
# criando uma declaração SELECT * FROM users
sql = select(User)
print(sql)

# executando a declaração a cima
resultado = session.execute(sql).scalars().all()
# aqui você verá uma lista com os nomes dos usuários
print (sql)
print(resultado)

print("\n------------------- select 2 -----------------------")
sql2 = select(User).limit(3)
resultado = session.execute(sql2).scalars().all()
print (sql2)
print(resultado)

print("\n------------------- select 3 -----------------------")
sql3 = select(User).where(User.nome.startswith('A'))
resultado = session.execute(sql3).scalars().all()
print (sql3)
print(resultado)


print("\n------------------- insert 1 -----------------------")
sql4 = insert(User).values(nome="José Silva")
print(sql4)
session.execute(sql4)
session.commit ()

