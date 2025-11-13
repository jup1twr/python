#   crie uma função que recebe uma lista de números e retorne
#   uma nova lista com os números ordenados em ordem crescente
#   ao fim, mostre ao usuário a lista original e a nova lista.
def crescente(list):
    list = [50,10,4,9,6,4,7,23,31,47,77] #  essa é a lista q vou ordenar
    ordem = sorted(list) #  sorted ordena a lista
    print(f"A lista original é {list}")
    print(f"A lista em ordem crescente é {ordem}")

crescente(())
#   a principal diferença é que sort() modifica a lista original (ordena "in-place") e retorna None (NADA),
#   enquanto sorted() cria e retorna uma nova lista ordenada, deixando a original inalterada. (nesse caso, a melhor para escolher)
#   O método sort() só funciona com listas, já a função sorted() pode ser aplicada a qualquer coisa (como strings, float, int), e sempre retorna uma lista. 
