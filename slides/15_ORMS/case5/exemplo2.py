from database.config import session, User, start_db, destroy_db
from sqlalchemy import select

start_db()

# outras opções de execução

declaracao = select(User)

# diferentes formas de usar scalars - Geral ResultScalar
resultado1 = session.execute(declaracao).scalars()
resultado2 = session.scalars(declaracao)

# diferentes formas de gerar o resultado em lista
resultado3 = session.execute(declaracao).scalars().all()
resultado4 = session.scalars(declaracao).all()

print(type(resultado1))
print(type(resultado2))

print(type(resultado3))
print(type(resultado4))

destroy_db()