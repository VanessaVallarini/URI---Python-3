ENTRADA = input().split(" ")
A, B, C = ENTRADA

TRIANGULO = (float(A) * float(C))/2
CIRCULO = 3.14159 * float(C) * float(C)
TRAPEZIO = float(C) *(float(A) + float(B)) / 2
QUADRADO = float(B) * float(B)
RETANGULO = float(A) * float(B)

print("TRIANGULO: %0.3f" % TRIANGULO)
print("CIRCULO: %0.3f" % CIRCULO)
print("TRAPEZIO: %0.3f" % TRAPEZIO)
print("QUADRADO: %0.3f" % QUADRADO)
print("RETANGULO: %0.3f" % RETANGULO)
