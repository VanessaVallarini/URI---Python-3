n=int(input())

for i in range(0,n):
    cont=0
    x=int(input())
    for i in range(1,x+1):
        if x%i==0:
            cont+=1
    if cont > 2:
        print(x,"nao eh primo")
    else:
        print(x,"eh primo")
