listNum = []
cont = 0

x = int(input())

while (cont<x):
  a, b = map(int, input().split())
  
  if a>b:
    listNum.append([b, a])
  elif a<b:
    listNum.append([a, b])
  else:
    listNum.append([a, b])
  
  cont+=1
  
for n in listNum:
  soma = 0
  for i in range(n[0]+1, n[1]):
    if (i%2!=0):
      soma += i
  print(soma)
