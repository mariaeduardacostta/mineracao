

print("ESCOLHA UMA OPERACAO")
print("1 - Adicao")
print("2 - Subtracao")
print("3 - Divisao")
print("4 - Multiplicacao")

op = int(input())

n1 = int(input("Num 1: "))
n2 = int(input("Num 2: "))

if(op == 1):
  print(f"{n1} + {n2} = {n1+n2}")
elif(op == 2):
  print(f"{n1} - {n2} = {n1-n2}")
elif(op == 3):
  print(f"{n1} / {n2} = {n1/n2}")
elif(op == 4):
  print(f"{n1} * {n2} = {n1*n2}")