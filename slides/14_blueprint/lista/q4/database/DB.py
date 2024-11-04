import MySQLdb
from sqlite3 import Connection, Row, connect
import sqlite3

class Database:           
    database: str
    type: str         
    @classmethod
    def factory(cls, type, **kwargs):
        if type == 'SQLITE':
            return Sqlite3(kwargs['database'], kwargs['sql_file'])
        elif type == 'MYSQL':
            return MySQL(kwargs['host'], kwargs['user'], kwargs['passw'], kwargs['port'], kwargs['database'])
        
    def save(self, objeto):
        #obter nome da classe
        classname = type(objeto).__name__ + 's'
        #dicionário de dados do objeto
        objeto_dict = objeto.__dict__
        # colunas da tabela    
        columns = ','.join(objeto_dict.keys())
        if self.type == "SQLITE":
            flag = ','.join('?' for x in range(len(objeto_dict)))
        elif self.type == "MYSQL":
            flag = ','.join('%s' for x in range(len(objeto_dict)))        
        
        sttm = f"INSERT INTO {classname}({columns}) values({flag})"
        return {
            'sql': sttm, 
            'data': tuple(objeto_dict.values())
        }
        
        
class Sqlite3(Database):
    conn: Connection
    def __init__(self, database: str, sql_file: str) -> None:        
        self.type = 'SQLITE'
        self.database = database

        try:
            with open(sql_file) as file:
                self.conn = sqlite3.connect(database)
                self.conn.executescript(file.read())
                self.conn.commit()
        except:
            raise('Não foi possível conectar')
        
    def save(self, objeto) -> None:
        sttm = super().save(objeto)        
        self.conn.execute(sttm['sql'], sttm['data'])
        self.conn.commit()     
    
class MySQL(Database):
    host: str
    user: str
    passw: str
    port: int    
    def __init__(self, host, user, passw, port, database) -> None:        
        self.host = host
        self.user = user
        self.passw = passw
        self.port = port
        self.database = database
        self.type = 'MYSQL'
        
        try:                                    
            self.db = MySQLdb.connect(host=self.host,
                user=self.user,
                port=self.port,
                password=self.passw,
                database=self.database)
        except:
            raise('Erro ao tentar conectar')
    
    def save(self, objeto):
        sttm = super().save(objeto)
        cursor = self.db.cursor()        
        cursor.execute(sttm['sql'], sttm['data'])
        self.db.commit()