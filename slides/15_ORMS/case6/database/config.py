from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database.models import Base, User, Admin, Company, Recipe
from faker import Faker
import random

engine = create_engine('sqlite:///projeto.db')
session = Session(bind=engine)


# criar o banco
def start_db(num_users=20, num_recipes=40, num_companies=20, admins=10):
    Base.metadata.create_all(bind=engine)
    faker = Faker()

    for _ in range(num_users):
        user = User(name=faker.unique.name())
        session.add(user)
    session.commit()

    for _ in range(num_recipes):
        recipe = Recipe(name=faker.unique.name(), user_id=random.randint(1,num_users))
        session.add(recipe)
    session.commit()

    for _ in range(admins):
        admin = Admin(name=faker.unique.name())
        session.add(admin)
    session.commit()

    for _ in range(num_companies):
        company = Company(name=faker.unique.name(), admin_id=random.randint(1,admins))
        session.add(company)
    session.commit()


# destruir o banco
def destroy_db():
    Base.metadata.drop_all(bind=engine)