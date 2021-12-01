import math
import numpy
graus = float(input("Informe um valor em graus"))

rad = numpy.deg2rad(graus)

seno = math.sin(rad)
cos = math.cos(rad)
tang = math.tan(rad)

print(f"Seno: {seno}\nCosseno: {cos}\nTangente: {tang}")