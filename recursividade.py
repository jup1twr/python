#funcao recursiva é a funcao que CHAMA A SI MESMA dentro de sua def
def fatorial(n):
    #calcular o fatorial do N recursivamente
    if n <= 1:
        return 1
    return n * fatorial(n - 1)
print(fatorial(5)) #o parentese roxo é o valor que decidi para a variavel
