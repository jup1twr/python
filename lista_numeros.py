#   implemente uma função que receba uma lista de números e 
#   retorne o maior valor dessa lista.

def maior(lista):
    if not lista:
        return None
    maior = lista[0] #  usamos lista[0] para ter um ponto de partida, já que o python começa a contar no ZERO.
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

numeros = []
quantidade = int(input("Quantos números têm na sua lista? "))

for i in range(quantidade):
    numero = float(input(f"Digite o número {i+1}"))
    numeros.append(numero) #adicionar dentro do vetor ao final da lista um valor novo.
    
print(f"O maior número é {maior(numeros)}")