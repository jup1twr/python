#   uma lista é como uma "caixa" onde você pode guardar vários itens em ordem

#   criando uma lista
frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]
misturada = ["texto", 42, 3.14, True]

#   acessando elementos

frutas = ["maçã", "banana", "laranja"]

print(frutas[0])    #   primeiro elemento: "maçã"
print(frutas[1])    #   segundo elemento: "banana"
print(frutas[-1])   #   último elemento: "laranja"

#   modificando elementos
frutas = ["maçã", "banana", "laranja"]
frutas[1] = "morango"  # Troca "banana" por "morango"
print(frutas)  # ["maçã", "morango", "laranja"]

#   adicionando elementos
frutas = ["maçã", "banana"]

#   adiciona no final
frutas.append("laranja")        #   ["maçã", "banana", "laranja"]

#   adiciona em posição específica
frutas.insert(1, "uva")         #   ["maçã", "uva", "banana", "laranja"]

#   removendo elementos:
frutas = ["maçã", "banana", "laranja"]

#   pelo valor
frutas.remove("banana")         #   ["maçã", "laranja"]

#    pelo índice
del frutas[0]                   #   ["laranja"]

#   remove e retorna o último
ultima = frutas.pop()           #   ultima = "laranja", frutas = []

#   tamanho da lista
frutas = ["maçã", "banana", "laranja"]
print(len(frutas))  # 3

#   verificar se existe
frutas = ["maçã", "banana", "laranja"]
print("maçã" in frutas)    # True
print("uva" in frutas)     # False

#   juntar listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
juntadas = lista1 + lista2  # [1, 2, 3, 4, 5, 6]

#   fatiamento (slicing)
numeros = [0, 1, 2, 3, 4, 5]
print(numeros[1:4])    # [1, 2, 3] (do índice 1 ao 3)
print(numeros[:3])     # [0, 1, 2] (do início ao índice 2)
print(numeros[3:])     # [3, 4, 5] (do índice 3 ao final)

### percorrendo uma lista com: for loop
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

#   com índice
frutas = ["maçã", "banana", "laranja"]
for i, fruta in enumerate(frutas):
    print(f"Índice {i}: {fruta}")

#   métodos úteis
numeros = [3, 1, 4, 1, 5, 9]

#   ordenar
numeros.sort()              # [1, 1, 3, 4, 5, 9]

#   inverter ordem
numeros.reverse()           # [9, 5, 4, 3, 1, 1]

#   contar ocorrências
print(numeros.count(1))     # 2

#   encontrar índice
print(numeros.index(4))     # 2

# lista de compras
compras = []

while True:
    item = input("Digite um item (ou 'sair' para terminar): ")
    if item.lower() == "sair":
        break
    compras.append(item)
print("\nSua lista de compras:")
for i, item in enumerate(compras, 1):
    print(f"{i}. {item}")
