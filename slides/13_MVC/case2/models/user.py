from database import get_connection

class User:
    def __init__(self, email, nome):
        self.email = email
        self.nome = nome
        
    def save(self):
        pass
    
    def get(cls, email):
        pass