from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from .models import Student, Course, Base
from faker import Faker
import random
import os.path

engine = create_engine("sqlite:///students_courses.db")
session = Session(bind=engine)

def start_db(num_students=10, num_courses=5):
    fake = Faker()

    # Criar banco de dados
    Base.metadata.create_all(bind=engine)

    # Criar cursos fictícios
    courses = [Course(name=fake.unique.word().capitalize()) for _ in range(num_courses)]
    session.add_all(courses)
    session.commit()

    # Criar estudantes fictícios e vinculá-los a cursos aleatórios
    for _ in range(num_students):
        student = Student(
            name=fake.name(),
            age=random.randint(18, 30)
        )
        # Associar a cursos aleatórios
        student.courses = random.sample(courses, k=random.randint(1, len(courses)))
        session.add(student)
    
    session.commit()

    print(f"Adicionados {num_students} estudantes e {num_courses} cursos ao banco de dados.")


def destroy_db():
    Base.metadata.drop_all(bind=engine)

