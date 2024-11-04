

def soma (a: int, b: int) -> int:
    """Retorna a soma de dois inteiros"""    
    return a + b

def subtracao (a: int, b: int) -> int:
    """Retorna a subtração de dois inteiros"""    
    return a - b

def multiplicacao (a: int, b: int) -> int:
    """Retorna a multiplicação de dois inteiros"""
    return a * b

def resto (a: int, b: int) -> int:
    """Retorna o resto da divisão entre dois inteiros"""  
    try:
        return a % b
    except:        
        raise ArithmeticError("Não é possível realizar divisão por 0")
    