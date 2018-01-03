T=int(input())
linha=(input().split())
soma=0
for i in range(5):
    if int(linha[i]) == T:
        soma+=1

print(soma)    

