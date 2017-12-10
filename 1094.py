n=int(input())

totalCobaias=0
ratos=0
sapos=0
coelhos=0

for i in range (n):
    x = input().split()
    totalCobaias += int(x[0])
    if x[1] == "R":
        ratos += int(x[0])
    if x[1] == "S":
        sapos += int(x[0])
    if x[1] == "C":
        coelhos += int(x[0])
        
percentualRatos= (ratos/totalCobaias)*100
percentualSapos= (sapos/totalCobaias)*100
percentualCoelhos= (coelhos/totalCobaias)*100



print("Total:",totalCobaias,"cobaias")
print("Total de coelhos:", coelhos)
print("Total de ratos:", ratos)
print("Total de sapos:", sapos)
print("Percentual de coelhos: %0.2f" %percentualCoelhos,"%")
print("Percentual de ratos: %0.2f" %percentualRatos,"%")
print("Percentual de sapos: %0.2f" %percentualSapos,"%")    
