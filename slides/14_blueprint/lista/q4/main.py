from database.DB import *
import os
from models.estudante import Estudante

# encontrar caminho raiz do exemplo
full_path = os.path.abspath(__file__)
dir_name = os.path.dirname(full_path)

# definir onde ficará o banco 
database = dir_name+"\\instance\\teste.db"
# localiza o arquivo sqlite
sqlfile = dir_name+"\\instance\\sqlite.sql"


# Conexão com banco MYSQLs
db = MySQL("localhost", "root", "romerito", 3306, 'TESTE')

# conexão com banco SQLITE3
db2 = Sqlite3(database=database, sql_file=sqlfile)

# Conexão com banco SQLITE e MYSQL usando fábrica de conexões.
db3 = Database.factory(type='SQLITE', database=database, sql_file=sqlfile)
db4 = Database.factory(type='MYSQL', host="localhost", user="root", passw="romerito", port=3306, database='TESTE')

# insert no banco SQLITE
e = Estudante('julio', 123123)
db3.save(e)

# Insert no banco MYSQL
db4.save(e)


