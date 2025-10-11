print("Olá! Vamos descobrir a tabuada?")
print("===============================")
num = int(input("Digite um número: "))
print("===============================")

print(f"A tabuada do {num} é: ")
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")
