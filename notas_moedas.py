valor = float(input())
centavos = int(valor * 100 + 0.001)
notas_100 = centavos // 10000
centavos %= 10000
notas_50 = centavos // 5000
centavos %= 5000
notas_20 = centavos // 2000
centavos %= 2000
notas_10 = centavos // 1000
centavos %= 1000
notas_5 = centavos // 500
centavos %= 500
notas_2 = centavos // 200
centavos %= 200
moedas_1 = centavos // 100
centavos %= 100
moedas_050 = centavos // 50
centavos %= 50
moedas_025 = centavos // 25
centavos %= 25
moedas_010 = centavos // 10
centavos %= 10
moedas_005 = centavos // 5
centavos %= 5
moedas_001 = centavos
print("NOTAS:")
print(f"{notas_100} nota(s) de R$ 100.00")
print(f"{notas_50} nota(s) de R$ 50.00")
print(f"{notas_20} nota(s) de R$ 20.00")
print(f"{notas_10} nota(s) de R$ 10.00")
print(f"{notas_5} nota(s) de R$ 5.00")
print(f"{notas_2} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{moedas_1} moeda(s) de R$ 1.00")
print(f"{moedas_050} moeda(s) de R$ 0.50")
print(f"{moedas_025} moeda(s) de R$ 0.25")
print(f"{moedas_010} moeda(s) de R$ 0.10")
print(f"{moedas_005} moeda(s) de R$ 0.05")
print(f"{moedas_001} moeda(s) de R$ 0.01")