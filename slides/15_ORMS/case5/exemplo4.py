from database.config import session, User, start_db, destroy_db
from sqlalchemy import select, desc

start_db()

# consulta os elementos ordenados pelo nome
declaracao = select(User).order_by(User.nome)
print(declaracao)
# imprime nomes de usuários em ordem crescente
for user in session.execute(declaracao):
    print(user)

# imprime nomes de usuários em ordem decrescente
declaracao = select(User).order_by(desc(User.nome))
print(declaracao)
for user in session.execute(declaracao):
    print(user)

destroy_db()