X=float(input())

calculo=X

for i in range (0,100):
    print("N["+str(i)+"] =","%0.4f" %calculo)
    calculo = X/2
    X=calculo
    

