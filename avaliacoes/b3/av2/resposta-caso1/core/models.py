from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from database import Base

class User(UserMixin, Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str] = mapped_column(String(50),unique=True)
    email: Mapped[str] = mapped_column(String(50), unique=True)
    senha: Mapped[str]
    

