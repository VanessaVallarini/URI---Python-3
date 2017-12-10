idade=1
soma=0
cont=0
media=0

while idade > 0:
    idade=int(input())
    if idade > 0:
        soma += idade
        cont += 1
        media = soma/cont
   
print("%0.2f" %media)
