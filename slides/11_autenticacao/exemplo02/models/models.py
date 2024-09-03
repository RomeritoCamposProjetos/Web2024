from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

database = 'database.db'

def obter_conexao():
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    return conn

class User(UserMixin):
    def __init__(self, email, password):
        self._id = None
        self._email = email
        self._password = password
        self._hash = generate_password_hash(password)
        
    # 5 - sobresrever get id do UserMixin
    def get_id(self):
        return str(self._id)
        
    
    # usada para definir senha como uma propriedade
    @property
    def password(self):
        return self._hash
    
    # limita o acesso a senha para atribuição de valor
    # sempre salva o hash a partir da senha
    @password.setter
    def password(self, password):
        self._hash = generate_password_hash(password)       
    
    # ----------métodos para manipular o banco--------------#
    def save(self):        
        conn = obter_conexao()  
        cursor = conn.cursor()      
        cursor.execute("INSERT INTO users(email, password) VALUES (?,?)", (self._email, self._hash))
        # salva o id no objeto recem salvo no banco
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()
        return True
    
    @classmethod
    def get(cls,user_id):
        conn = obter_conexao()
        user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        conn.close()
        if user:
            loaduser = User(user['email'] , user['password'])
            loaduser._id = user['id'],
            return loaduser
        else:
            return None
    
    @classmethod
    def exists(cls, email):
        conn = obter_conexao()
        user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        conn.close()
        if user: #melhorar esse if-else
            return True
        else:
            return False
    
    
    
    @classmethod
    def all(cls):
        conn = obter_conexao()
        users = conn.execute("SELECT id, email FROM users").fetchall()
        conn.close()
        return users
    
    @classmethod
    def get_by_email(cls,email):
        conn = obter_conexao()
        user = conn.execute("SELECT id, email, hash FROM users WHERE email = ?", (email,)).fetchone()
        conn.close()
        return user
    
        
    

    