from database.config import start_db, destroy_db, session
from sqlalchemy import select
from database.models import Student, Course, student_course_table

start_db(num_students=100, num_courses=10)

# print dos cursos
declaracao = select(Course)
cursos = session.scalars(declaracao).all()
for course in cursos:
    print(course)

# selecionar alunos com base no curso de id=5

print()
print(' # Escolha do Curso')
declaracao2 = select(Course).where(Course.id == 5)
curso = session.scalars(declaracao2).one()

# join Many-to-Many
# Obter os alunos que estudam o no curso cujo id=5
declaracao3 = (
    select(Student, Course)
    .join(student_course_table, Student.id == student_course_table.c['student_id'])
    .join(Course, Course.id == student_course_table.c['course_id'])
    .where(Course.id == curso.id)
)

print()
print(' ## Consulta')
print(declaracao3)
# consulta gera uma Rows (que contém o estudante e o curso)
resultado3 = session.execute(declaracao3).all()

print()
print(' ## Consulta')
for stu in resultado3:
    print(stu[0], stu[1])


# ---------------------------------------------------------------
# obtendo o mesmo resultado com session.query()

# obter o nome dos cursos de cada um dos alunos
resultado4 = (
    session.query(Student, Course.name)
    .where(Student.id == student_course_table.c['student_id'])
    .where(Course.id == student_course_table.c['course_id'])
    )
    
for user in resultado4:
    print(user)

destroy_db()