n = int(input())
aux=0

if n %2!=0:
    aux=n+1
    cont=0
    cont2=0
    print("N["+str(cont)+"] =", n)
    cont =1
    while cont <= 9:
        print("N["+str(cont)+"] =", aux)
        cont2=aux
        aux=cont2+cont2
       
        cont+=1
        
else:
    aux=n
    cont=0
    cont2=0
    while cont <= 9:
        print("N["+str(cont)+"] =", aux)
        cont2=aux
        aux=cont2+cont2
       
        cont+=1


