import math
total = int(input("Informe um numero de segundos: "))

horas = math.floor(total / 3600)
minutos = math.floor((total - (horas * 3600)) / 60)
segundos = math.floor(total % 60)

print(f"{total} segundos sao {horas}:{minutos}:{segundos}")