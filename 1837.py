import math
a, b = map(int, input().split())

if b > 0:
    quociente = math.floor(a / b)
else:
    quociente = math.ceil(a / b)

resto = a - quociente * b

print(quociente,resto)
