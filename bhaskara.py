import math
A, B, C = map(float, input().split())
delta = B**2 - 4 * A * C
if A == 0 or delta < 0:
    print("Impossível calcular")
else:
    raiz = math.sqrt(delta)
    R1 = (-B + raiz) / (2 * A)
    R2 = (-B - raiz) / (2 * A)
    print(f"R1 =={R1:.5f}")
    print(f"R2 = {R1:.5f}")