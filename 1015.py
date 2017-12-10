import math

LINHA1 = input().split(" ")
LINHA2 = input().split(" ")
X1, Y1 = LINHA1
X2, Y2 = LINHA2

DISTANCIA = math.sqrt(((float(X2) - float(X1))*(float(X2) - float(X1))) + ((float(Y2)-float(Y1)) *(float(Y2)-float(Y1))))
print("%0.4f" %DISTANCIA)
