from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

"""Classe Base

A ideia central do ORM é fazer o mapeamento objeto-relacional.
A classe Base é usada para permitir o mapeamento nas suas subclasses
fornecendo a estrutura necessária para o ORM compreender a criação 
dos demais modelos.

"""
class Base(DeclarativeBase):
    pass

"""
Taken together, the combination of a string table name as well as a list of column declarations is known in SQLAlchemy as table metadata.
"""
class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str]