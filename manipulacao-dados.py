nome_completo = input("Digite seu nome e sobrenome completo: ")
    #versão original
print(nome_completo)

    #letras maiúsculas
print(nome_completo.upper())

    #retirar o espaço em excesso
print(nome_completo.strip())

    #letra minuscula
print(nome_completo.lower())

#com vetor, começamos com o zero, logo "ricardo" seria 0. vetor sempre começa com 0
#vetor == ["ricardo", "onaip", "andrea"] # type: ignore

#primeiro nome, começa com 0 também, split divide

nomes = nome_completo.split()
print(nomes[0])
print(len(nomes))

#deixa a primeira letra de cada palavra maiúscula
print(nome_completo.title())

#substituir um texto por outro
print(nome_completo.replace("Oliveira", "Firjan"))

