idade = int(input("Digite sua idade: "))

if idade < 13: #se idade menor que 13, leia criança
    print("Criança")
elif idade < 20:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")