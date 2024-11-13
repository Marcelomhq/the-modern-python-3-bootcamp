# Escreva uma funcao que conta quantas vezes cada letra tem em uma palavra ou frase.

def conta_letras(palavra):
    contador = {}
    for letra in palavra:
        contador[letra.lower()] = contador.get(letra.lower(), 0) + 1
    return contador

print(conta_letras("Meu nome eh marcelo"))