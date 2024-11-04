from models.estudante import Estudante
from models.livro import Livro

if __name__ == '__main__':
    
    livro = Livro('Python Fluent', 'Luciano Ramalho')
    estudante = Estudante ('José', 123123)
    
    # print do objeto
    print(estudante)
    print(livro)
    
    # print do objeto como um dicionário
    print (estudante.__dict__)
    print (livro.__dict__)
    