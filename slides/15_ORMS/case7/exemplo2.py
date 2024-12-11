from database.config import destroy_db, start_db, session
from sqlalchemy import select
from database.models import Student, Course, student_course_table
from sqlalchemy import func


start_db(num_students=100)

# agrupar os alunos por curso e contabilizar quantos estudantes há por curso
declaracao = select(Course, func.count(Student.id).label('Numero Estudantes')).join(
        student_course_table, Course.id == student_course_table.c['course_id']
    ).join(
        Student, student_course_table.c['student_id'] == Student.id
    ).group_by(Course.id)

print(declaracao)

for g in session.execute(declaracao):
    print(g[0], g[1])
    

destroy_db()
