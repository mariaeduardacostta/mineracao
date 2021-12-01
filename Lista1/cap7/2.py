lista = []

nome = input("Adicionar nome a lista: ")

while nome != "":
  lista.append(nome)
  nome = input("Adicionar nome a lista: ")

d = {}

for nome in lista:
  val = d.get(nome)
  if(val):
    d[nome] = val + 1
  else:
    d[nome] = 1

print(d)