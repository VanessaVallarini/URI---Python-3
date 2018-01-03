L=int(input())
T=(input())

cont=0
cont2=0
soma=0
media=0

for i in range(12):
    for j in range(12):
        n=float(input())
        if i==L:
            soma+=n
            cont+=1
            media=soma/cont

if T.upper() == "S":
    print(soma)
else:
    print(media)
