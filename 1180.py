n=int(input())

line=list(map(int,input().split()))

menorValor=0
posicao=0

for i in range(n):
    if int(line[i]) < menorValor or menorValor == 0:
        menorValor = int(line[i])
        posicao = i

print("Menor valor:",menorValor)
print("Posicao:",posicao)    
