n,m=map(int,input().split())
cont=n
for i in range(m):
    acao=input()
    if acao == "fechou":
        cont+=1
    if acao == "clicou":
        cont-=1
print(cont)    
