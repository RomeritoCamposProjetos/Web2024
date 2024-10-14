from case2.database import get_connection

class User:
    def __init__(self, email, nome):
        self.email = email
        self.nome = nome
        
    def save(self):
        conn = get_connection()
        conn.execute("INSERT INTO users(email, nome) values(?,?)", (self.email, self.nome))
        conn.commit()
        conn.close()
        return True
    
    @classmethod
    def all(cls):
        conn = get_connection()
        users = conn.execute("SELECT * FROM users").fetchall()
        return users
       