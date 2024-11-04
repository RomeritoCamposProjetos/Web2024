import matematica
from matematica import *

if __name__ == '__main__':
    a = int(input("Digite o primeiro operando: "))
    b = int(input("Digite o segundo operando:"))
    
    print (matematica.multiplicacao(a, b))
    print(resto(a, b))
    