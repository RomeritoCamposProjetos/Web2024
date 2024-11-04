from database.DB import *
import os
from models.estudante import Estudante

db = MySQL("localhost", "root", "romerito", 3306, 'TESTE')

# encontrar caminho raiz do exemplo
full_path = os.path.abspath(__file__)
dir_name = os.path.dirname(full_path)

# definir onde ficará o banco 
database = dir_name+"\\instance\\teste.db"
# localiza o arquivo sqlite
sqlfile = dir_name+"\\instance\\sqlite.sql"

print(database)
print(sqlfile)

db2 = Sqlite3(database=database, sql_file=sqlfile)

db3 = Database.factory(type='SQLITE', database=database, sql_file=sqlfile)
db4 = Database.factory(type='MYSQL', host="localhost", user="root", passw="romerito", port=3306, database='TESTE')

e = Estudante('julio', 123123)
db3.save(e)

db4.save(e)


