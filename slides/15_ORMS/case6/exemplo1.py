from database.config import session, destroy_db, start_db
from database.models import User, Recipe, Admin, Company

start_db()

# Testando relacionamento User-Recipe
user = session.query(User).first()
print(user.recipes)
recipe = session.query(Recipe).first()
print(recipe.user)

# print(session.query(Company).first().admin)
company = session.query(Company).first()
print(company.admin)

destroy_db()