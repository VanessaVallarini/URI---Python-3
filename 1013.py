import math 

ENTRADA = input().split(" ")

A, B, C = ENTRADA
MAIOR = (int(A) + int(B) + abs(int(A) - int(B)))  / 2 
RESULTADO = (int(MAIOR) + int(C) + abs(int(MAIOR) - int(C)))/2

print("%d eh o maior" %RESULTADO)
