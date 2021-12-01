valor = int(input("Informe um valor: "))
notas = 0

while(valor/100 >= 1):
  notas += 1
  valor -= 100

while(valor/50 >= 1):
  notas += 1
  valor -= 50

while(valor/10 >= 1):
  notas += 1
  valor -= 10

while(valor/1 >= 1):
  notas += 1
  valor -= 1

print(f"Sao necessarias no minimo {notas} notas")