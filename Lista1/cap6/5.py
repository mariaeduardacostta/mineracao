def fatora(n):
  if(n == 0):
    return
  elif(n == 1):
    return 1
  else:
    fatoriais = []

    for i in range(2, n+1):
      while(n % i == 0):
        n = n/i
        fatoriais.append(i)
    
    return fatoriais

n = int(input("Informe um numero para fatorar: "))

print(fatora(n))