n5par = []
n5impar = []

qp=0
qi=0
contTotal=0
contaux=5
contaux2=5

while contTotal <= 14:
    x=int(input())

    if x%2 == 0:
        n5par.append(x)
        qp+=1

        if qp ==5:
            for j in range(5):
                print("par["+str(j)+"] =",n5par[j])
            qp=0

        
    else:
        n5impar.append(x)
        qi+=1

        if qi ==5:
            for k in range(5):
                print("impar["+str(k)+"] =",n5impar[k])
            qi=0
        
         
    
    contTotal+=1

for m in range(qi):
    print("impar["+str(m)+"] =",n5impar[contaux2])
    contaux2+=1

for i in range(qp):
    print("par["+str(i)+"] =",n5par[contaux])
    contaux+=1
       
