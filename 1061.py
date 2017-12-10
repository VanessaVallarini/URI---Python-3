di = input().split(" ")
w = int(di[1])
hi = input().split(" ")
x = int(hi[0])
y = int(hi[2])
z = int(hi[4])

df = input().split(" ")
w1 = int(df[1])
hf = input().split(" ")
x1 = int(hf[0])
y1 = int(hf[2])
z1 = int(hf[4])

#Execução

dia = w1 - w #Dia final - dia inicial '9 - 5 == 4'

hora = x1 - x #Hora final - hora incial '06 - 08 == -2'
if(hora < 0):#entra neste if
	hora = 24 + hora #24 + (-2) == 22
	dia = dia - 1 #dia = 4 - 1

minuto = y1 - y #Minuto final - minuto inicial '13 - 12 == 1'
if(minuto < 0): #Não entra neste if 
	minuto = 60 + minuto
	hora = hora - 1
	
segundos = z1 - z #Segundos inicial - segundos final '23 - 23 == 0'
if(segundos < 0):
	segundos = 60 + segundos
	minuto = minuto - 1

if(dia <= 0):
	dia = 0

print("%d dia(s)" %dia)
print("%d hora(s)" %hora)
print("%d minuto(s)" %minuto)
print("%d segundo(s)" %segundos)
    

