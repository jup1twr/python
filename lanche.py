codigo, quantidade = map(int, input().split())
if codigo == 1:
    preco = 4.00
elif codigo == 2:
    preco = 4.50
elif codigo == 3:
    preco = 5.00
elif codigo == 4:
    preco = 2.00
elif codigo == 5:
    preco = 1.50
else:
    preco = 0.00
total = preco * quantidade
print(f"Total: R$ {total:.2f}")