from database.config import session, User, start_db, destroy_db
from sqlalchemy import select

start_db()

# Select padrão
# utiliza o modelo para construir a busca
# utiliza a função select() - construr de consulta
declaracao = select(User)

# print(declaracao)

# produz um objeto ResultScalar - que pode ser percorrido no FOR
resultado1 = session.scalars(declaracao)

# produz uma lista de objetos baseado no modelo User
resultado2 = session.scalars(declaracao).all()

# veja os tipos - 
# https://stackoverflow.com/questions/78703317/difference-between-scalars-all-and-list-scalars-in-sqlalchemy
print(type(resultado1))
print(type(resultado2))

# mesmo resultado
for x in resultado1:
    print(x)
for x in resultado2:
    print(x)

destroy_db()