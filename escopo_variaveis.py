#   as variaveis tem diferentes escopos (visibilidade)
x = 10
#   a variavel global é :
def funcao ():
    # a variavel local é :  
    y = 5
    print(f" Dentro da função - X:{x}, y: {y}")
    return y #return transforma o y em variavel global.

y = funcao() #y vai retornar a funcao
funcao() #  saída, dentro da função - X = 10, Y = 5
#   fora da funcao, variável Y não está disponível.
print(f"Fora da função - X{x}")
print(f"Fora da função - Y{y}")
#   erro: nome Y não está definido.
       