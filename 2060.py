n=int(input())
linha=input().split()

cont2=0
cont3=0
cont4=0
cont5=0

for i in range(n):
    
    if (int(linha[i]))%2==0:
        cont2+=1
    if (int(linha[i]))%3==0:
        cont3+=1
    if (int(linha[i]))%4==0:
        cont4+=1
    if (int(linha[i]))%5==0:
        cont5+=1
        
print(cont2,"Multiplo(s) de 2")      
print(cont3,"Multiplo(s) de 3") 
print(cont4,"Multiplo(s) de 4")  
print(cont5,"Multiplo(s) de 5")

