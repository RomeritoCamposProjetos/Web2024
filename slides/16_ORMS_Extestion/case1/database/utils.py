from faker import Faker
from database import db
from database.models import *

def start_db ():
    faker = Faker()
    for x in range(100):
        user = User(name=faker.name(), email=faker.unique.email())
        db.session.add(user)
    db.session.commit()