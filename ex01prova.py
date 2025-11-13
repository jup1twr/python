def classificar_idade(idade):
    idade = int(input("Digite uma idade: "))
    if idade < 0:
        return "Idade inválida"
    elif idade < 12:
        return "Criança"
    elif idade >= 12 and idade < 18:
        return "Adolescente"
    elif idade >= 18 and idade < 60:
        return "Adulto"
    else:
        return "Idoso"
