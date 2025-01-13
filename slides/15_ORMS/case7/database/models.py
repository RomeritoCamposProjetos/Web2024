from sqlalchemy import Table, ForeignKey, Column, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List

# Base para mapeamento declarativo
class Base(DeclarativeBase):
    pass

# Tabela associativa para a relação muitos-para-muitos
student_course_table = Table(
    "student_course",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True),
)

# Entidade Estudante
class Student(Base):
    __tablename__ = "students"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    
    # Relacionamento com cursos
    courses: Mapped[list["Course"]] = relationship(
        secondary=student_course_table, back_populates="students"
    )

    def __repr__(self) -> str:
        return f"Student(id={self.id}, name='{self.name}', age={self.age})"

# Entidade Curso
class Course(Base):
    __tablename__ = "courses"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    
    # Relacionamento com estudantes
    students: Mapped[list["Student"]] = relationship(
        secondary=student_course_table, back_populates="courses"
    )

    def __repr__(self) -> str:
        return f"Course(id={self.id}, name='{self.name}')"
    

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    admin: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True)
    # gerenciados: Mapped[List['User']] = relationship(remote_side='gerenciados')
