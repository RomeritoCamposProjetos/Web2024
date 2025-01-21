from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from typing import List
from sqlalchemy import String, ForeignKey

class Base(DeclarativeBase):
    pass

# backref vs back_populates
# https://medium.com/@kimberlymlove15/sqlalchemy-relationship-status-its-complicated-backref-vs-back-populates-9eaf07335a13

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    recipes = relationship('Recipe', backref='user')

    def __repr__(self):
        return f"(User={self.name})"

class Recipe(Base):
    __tablename__ = 'recipes'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id")) 

    def __repr__(self):
        return f"(Recipe={self.name})"


# usando back_populates
class Admin(Base):
    __tablename__ = 'admins'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    companies: Mapped[List["Company"]] = relationship(back_populates="admin")

class Company(Base):
    __tablename__ = 'companies'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)

    admin_id: Mapped[int] = mapped_column(ForeignKey("admins.id"))
    admin:Mapped["Admin"] = relationship(back_populates="companies")