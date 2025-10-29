import math
p1 = map(float, input().split())
x1, y1 = p1
p2 = map(float, input().split())
x2, y2 = p2
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"{distancia:.4f}")