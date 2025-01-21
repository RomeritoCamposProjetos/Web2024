from database.config import session, User, start_db, destroy_db
from sqlalchemy import select

start_db()

# exemplo de consulta usando operador AND
declaracao = select(User).where(User.nome.startswith('R'))
print(" --- Declaração SQL | String que iniciam com um valor dado --- ")
print(declaracao)

resultado = session.scalars(declaracao).all()

print(" --- Resultado ---")
for user in resultado:
    print(user) 

print ('--------------------------')

# Aplicando duas condições na claúsula Where
declaracao2 = select(User).where(
    User.nome.startswith('R'),
    User.nome.endswith('r'))

print(' --- Declaração SQL ---- ')
print(declaracao2)

resultado2 = session.scalars(declaracao2).all()

for user in resultado2:
    print(user) 

destroy_db()