def fibonacci(n):
  if(n <= 1):
    return n

  return fibonacci(n-1) + fibonacci(n-2)

n=int(input("Informe um numero: "))

for i in range(0, n):
  print(fibonacci(i))