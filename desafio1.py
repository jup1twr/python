#imprima números pares de 1 a 30 que são divisiveis por 3
numero = int
for numero in range (1,31):
    if numero % 2 == 0 and numero % 3 == 0:
        print(numero)
#para usar o if não necessariamente precisa ter um else