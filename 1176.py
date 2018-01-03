fib=[0,1]
aux1=0
aux2=1
for i in range(60):
    aux3=aux2+aux1
    fib.append(aux3)
    aux1=aux2
    aux2=aux3

t= int(input())
for i in range(t):
    n=int(input())
    print("Fib("+str(n)+") =",fib[n])
