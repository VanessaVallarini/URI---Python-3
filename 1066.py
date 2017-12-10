contPares=0
contImpares=0
contPositivos=0
contNegativos=0

for i in range(5):
    n = int(input())
    if n % 2 == 0:
        contPares += 1
    if n % 2 != 0:
        contImpares += 1
    if n > 0:
        contPositivos += 1
    if n < 0:
        contNegativos += 1

print(contPares,"valor(es) par(es)")
print(contImpares,"valor(es) impar(es)")
print(contPositivos,"valor(es) positivo(s)")
print(contNegativos,"valor(es) negativo(s)")
