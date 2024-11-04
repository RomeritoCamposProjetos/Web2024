from database import create_db, get_connection, save
from models.estudante import Estudante
from models.livro import Livro

if __name__ == '__main__':
    # a função create db invoca o acesso a conexão via get_connection
    create_db('teste.db', 'sqlite.sql')    
    create_db('novo.db', 'sqlite.sql')
    
    e = Estudante('João', 10)
    save(e, 'novo.db')
    
    l = Livro('Pense em Python', 'Luciano')
    save(l, 'novo.db')
    
    
    
    
    
        
        
    
    
    
    
    