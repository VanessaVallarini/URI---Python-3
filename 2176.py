frase=input()
cont=0
for i in range(len(frase)):
    if (int(frase[i])) == 1:
        cont+=1


if cont%2==0:
    print(frase+"0")
else:
    print(frase+"1")
        
