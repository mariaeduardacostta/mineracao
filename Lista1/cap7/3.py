msg = input("Informe uma mensagem")
palavras = msg.split(" ")
i = 0
for palavra in palavras:
  if(palavra[0].isupper() and palavra.isalpha()):
    j = 0
    p_list = list(palavra)
    for letra in p_list:
      p_list[j] = "*"
      j += 1
    palavras[i] = "".join(p_list)
  
  i += 1

msg = " ".join(palavras)
print(msg)