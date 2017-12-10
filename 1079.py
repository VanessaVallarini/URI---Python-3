N= int(input())

lista=[]
for i in range(N):
	valores= input()
	valores= valores.split()
	
	n1= float(valores[0])
	n2= float(valores[1])
	n3= float(valores[2])
	
	lista.append((n1*2+n2*3+n3*5)/10)
	
for i in range(N):
	print('{:.1f}'.format(lista[i]))
