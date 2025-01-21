from database.config import destroy_db, start_db, session
from sqlalchemy import select
from database.models import User

start_db()

admin = User(name='romero')
session.add(admin)
session.commit ()




# destroy_db()