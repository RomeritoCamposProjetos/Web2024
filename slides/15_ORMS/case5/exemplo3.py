from database.config import session, User, start_db, destroy_db
from sqlalchemy import select

start_db()

# limitar a busca a 5 usuários
declaracao = select(User).limit(5)

print(declaracao)
print()

resultado1 = session.scalars(declaracao).all()
for user in resultado1:
    print(user)

destroy_db()