from sqlalchemy import create_engine, ForeignKey, insert, select
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, relationship
from typing import List

engine = create_engine('sqlite:///teste.db')
session = Session(bind=engine)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str]
    gerente_id:Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True)
    gerenciados:Mapped[List['User']] = relationship('User', back_populates='gerente')
    gerente = relationship('User', back_populates='gerenciados', remote_side=[id])

    def __repr__(self):
        return f"(Nome={self.nome})"


Base.metadata.create_all(bind=engine)

user1 = User(nome='Bastim')
session.add(user1)

user2 = User(nome='Tião', gerente_id=1)
user3 = User(nome='Munda', gerente_id=1)

session.add_all([user2, user3])
session.commit()

print(user1.gerente) #None, não possui gerente
print(user1.gerenciados) # lista com dois usuários

Base.metadata.drop_all(bind=engine)
