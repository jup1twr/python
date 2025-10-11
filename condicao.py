# condição:  o programa verificará se a nota é menor que 5 (reprovado)
# senao, verifica se a nota é menor que 7 (recuperacao)
# caso nenhuma dessas condições seja verdadeira (aprovado)
nota = float(input("Digite sua nota: "))

if nota >= 0 and nota < 5.0:
    print("Reprovado!")
elif nota >= 0.0 and nota < 7.0:
    print("Recuperação!")
elif nota <= 10.0 and nota >= 7.0:
    print("Aprovado!")
else:
    print("Resposta inválida!")