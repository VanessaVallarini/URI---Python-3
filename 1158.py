n=int(input())
cont=1
cont2=1
soma=0


while cont <= n:
    x,y=map(int,input().split())
    cont2 = 0
    while cont2 < y:
        if x%2 != 0:
            soma += x
            cont2 += 1
        
            
        x += 1
    print(soma)
    soma=0
    cont += 1
