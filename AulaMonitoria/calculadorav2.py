def soma(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def multiplicacao(n1,n2):
    return n1*n2

def divisao(n1,n2):
    if n2 == 0:
        return "Erro, divisao por 0 n pode ser realizada"
    return n1/n2

def calculadora(func,n1,n2):
    operacoes = {
        'soma': soma,
        'subtracao': sub,
        'multiplicacao': multiplicacao,
        'divisao': divisao
        }
    if func not in operacoes:
        return f"Operacao {func} chamada invalida, opcoes validas sao {list(operacoes.keys())}"
    
    # resultado = func(n1,n2)
    resultado = operacoes[func](n1,n2)
    return f'Resultado da {func} dos numeros {n1} e {n2} eh de: {resultado}'

print(calculadora('soma',1,1))
print(calculadora('divisao',10,0))
print(calculadora('multiplicacao',10,10))
print(calculadora('potencia',10,10))