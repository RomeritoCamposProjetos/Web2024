from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
from faker import Faker
import os


# criar nomes de usuários para o banco
faker = Faker()

# definição de engine (dialeto) e criação da sessão
engine = create_engine('sqlite:///projeto.db')
session = Session(bind=engine)

# classe base para os demais modelos
class Base(DeclarativeBase):
    pass

# classe de exemplo
class User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str] = mapped_column(unique=True)

    def __repr__(self):
        return f"(nome={self.nome})"

def start_db():
    Base.metadata.create_all(bind=engine)
    for x in range(100):
        name = faker.name()
        user = User(nome = name)
        session.add(user)
    session.commit()

def destroy_db():
    session.close()
    engine.dispose()
    os.remove('projeto.db')