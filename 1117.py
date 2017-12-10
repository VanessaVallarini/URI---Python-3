nota=-1
cont=0
soma=0
media=0

while nota < 0.0 or nota > 10.0:
    while cont < 2:
        nota = float(input())
        if nota >= 0.0 and nota <= 10.0:
            soma+=nota
            media=soma/2
            cont+=1
        else:
            print("nota invalida")
            


print("media =",media)
