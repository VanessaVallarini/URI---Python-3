N=int(input())
aux=0.0
for i in range(N):
    aux = 1.0/(2 + aux)

aux = aux+1
print("%.10f" %aux)
 
