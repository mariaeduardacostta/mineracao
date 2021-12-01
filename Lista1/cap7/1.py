lista = ["nome1", "nome2", "nome1", "nome3", "nome4"]

d = {}

for nome in lista:
  val = d.get(nome)
  if(val):
    d[nome] = val + 1
  else:
    d[nome] = 1

print(d)