p=int(input())

calculo=0
soma=0

for i in range(p):
    cod,qtd=map(int,input().split())
    if cod == 1001:
        calculo = qtd*1.50
        soma+=calculo
    if cod == 1002:
        calculo2 = qtd*2.50
        soma+=calculo2
    if cod == 1003:
        calculo3 = qtd*3.50
        soma+=calculo3
    if cod == 1004:
        calculo4 = qtd*4.50
        soma+=calculo4
    if cod == 1005:
        calculo5 = qtd*5.50
        soma+=calculo5

print("%.2f" %soma)
