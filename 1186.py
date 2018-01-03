O = str(input())
linhas = 12
colunas = 12
matriz = []

for i in range(0,linhas):
  linha = []
  for j in range(0,colunas):
    numero = float(input())
    linha.append(numero)
  matriz.append(linha)

soma = 0  
soma_matriz = []

if O == 'S':
  aux = 1
  for i in range(11,0,-1):
    soma_matriz = []
    for j in range(aux,12):
      soma += matriz[i][j]
    soma_matriz.append(soma)
    aux += 1
  soma_total = sum(soma_matriz)
  
  print(soma_total)


elif O == 'M':
  aux = 1
  for i in range(11,0,-1):
    soma_matriz = []
    for j in range(aux,12):
        soma += matriz[j][i]
    aux += 1    
    soma_matriz.append(soma)
    soma = sum(soma_matriz)
  media = soma/66
  print('%.1f' %media)
