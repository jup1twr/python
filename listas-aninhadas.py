#lista que existe como elemento de outra lista
matriz = ["Willyan e Márcia",["Deniel", "Thais"]]
print(matriz)

A = [
    [2, 1, - 5],
    [3, 7, 0],
    [6, 4, 8]
]

print(A)
print(A[0][0])
#o primeiro decide a linha que vai mostrar e o segundo a coluna

for linha in matriz:
    for elemento in linha:
        print(elemento, end='')
#sufixed no final, prefixed no inicio