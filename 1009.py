NOME = (input())
SALARIO = float(input())
VENDAS = float(input())

TOTAL = float(VENDAS * (15/100) + SALARIO)

print("TOTAL = R$ %0.2f" % TOTAL)
