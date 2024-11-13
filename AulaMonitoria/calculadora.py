def soma(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def multiplicacao(n1,n2):
    return n1*n2

def divisao(n1,n2):
    return n1/n2

def calculadora(func,n1,n2):
    return f'Resultado da {func.__name__} dos numeros {n1} e {n2} eh de: {func(n1,n2)}'

print(calculadora(soma,1,1))