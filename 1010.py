LINHA1 = input().split(" ")
LINHA2 = input().split(" ")

COD1, QTD1, VALOR1 = LINHA1
COD2, QTD2, VALOR2 = LINHA2
TOTAL = (int(QTD1) * float(VALOR1)) + (int(QTD2) * float(VALOR2))

print("VALOR A PAGAR: R$ %0.2f" % TOTAL)
