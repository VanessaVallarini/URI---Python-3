resp = 1
soma = 0
media = 0
i = 0
aux=0
while(resp!=2):
  nota = float(input())
  
  if(nota >=0 and nota<=10):
    soma+=nota
    i+=1
  else:
    print("nota invalida")
  if (i==2):
    print("media = %0.2f" %(soma/2))
    soma=0
    i=0
  

    aux = float(input("novo calculo (1-sim 2-nao)\n"))
    while (aux>2):
      aux = float(input("novo calculo (1-sim 2-nao)\n"))
  resp = aux
