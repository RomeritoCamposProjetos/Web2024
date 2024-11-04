import sqlite3
import os

abs_path = os.path.abspath(__file__) #obtém localização deste arquivo (__init__)
dir_name = os.path.dirname(abs_path) # retira o nome do arquivo e fica com o diretórios

def get_connection(database):
    #o banco será salvo no mesmo local de __init__.py    
    filename = dir_name + "\\" + database    
    conn = sqlite3.connect( filename )
    conn.row_factory = sqlite3.Row    
    return conn

def create_db (database, sql):
    conn = get_connection(database) # obter conexão    
    filename =  dir_name + "\\" + sql    
    with open(filename) as file: 
        conn.executescript(file.read())
        conn.close()
        
        
def save(objeto, database):
    #obter nome da classe
    classname = type(objeto).__name__ + 's'
    #dicionário de dados do objeto
    objeto_dict = objeto.__dict__
    # colunas da tabela    
    columns = ','.join(objeto_dict.keys())
    flag = ','.join('?' for x in range(len(objeto_dict)))
        
    conn = get_connection(database)
    print(f"INSERT INTO {classname}({columns}) values({flag})", tuple(objeto_dict.values()))
    conn.execute (f"INSERT INTO {classname}({columns}) values({flag})", tuple(objeto_dict.values()))
    conn.commit()


    
    
