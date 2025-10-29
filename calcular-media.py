#   crie uma função chamada CALCULAR MÉDIA (notaA, notaB) que recebe 
#   as duas notas, calcula a média ponderada e retorna o resultado.

#   sem input   #
def calcular_media(nota_a, nota_b):
    mediapond = (nota_a * 2 + nota_b * 3) / 5
    print (f'A média ponderada é: {mediapond}')
calcular_media(7,8)