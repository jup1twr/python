#criando uma lista de notas
notas = [9.5, 7.0, 8.5, 5.5, 10.0] #tem que usar o colchete

#acessando a primeira nota (índice 0)
primeira_nota = notas[0]
print(f"A primeira nota foi: {primeira_nota}") #saída 9.5

#modificando a segund anota (índice 1)
notas[1] = 7.5
print(f"Lista de notas atualizada: {notas}")

notas.append(6.0) #append para adicionar nota
print(f"Lista após adicionar nota: {notas}")

notas.sort()
print(notas)

lista = [4, 1, 2, 3]
nova_lista = sorted(lista, reverse=True) #reverse=True decresente e reverse=False crescente
print(nova_lista)
print(lista)
