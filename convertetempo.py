segundos = int(input())
horas = segundos // 3600
segundos_restantes = segundos % 3600
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60
print(f"{horas}:{minutos}:{segundos}")