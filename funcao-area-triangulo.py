#faça uma função que recebe base e altura e retorna a área do triangulo.
def areatri (base,altura):
    area =base * altura / 2
    return f'A área do triângulo é: {area} cm²'
print(areatri(3, 6))