import math
graus = float(input("Informe um valor em graus"))

rad = (math.pi / 180) * graus

seno = math.sin(rad)
cos = math.cos(rad)
tang = math.tan(rad)

print(f"Seno: {seno}\nCosseno: {cos}\nTangente: {tang}")