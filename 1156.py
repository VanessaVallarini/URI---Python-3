S=1
cont = 2
aux = 2
for i in range (3,40,2):
    S = S + (i/cont)
    aux = aux + cont
    cont = aux
    
print("%.2f" %S)
