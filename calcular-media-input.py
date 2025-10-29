#   crie uma função chamada CALCULAR MÉDIA (notaA, notaB) que recebe    #
#   as duas notas, calcula a média ponderada e retorna o resultado.     #

#   com input   #
def calcular_media_input():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    result = (n1 * 2 + n2 * 3)/5
    return f'A média ponderada do aluno é {result}'
calcular_media_input(())