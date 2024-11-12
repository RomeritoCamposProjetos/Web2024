from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import db
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    senha: Mapped[str]
    def __init__(self, nome, email, senha) -> None:
        self.nome = nome
        self.email = email
        self.senha = generate_password_hash(senha)