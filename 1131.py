novoGrenal=1
somaGrenais=0
somaInter=0
somaGremio=0
empate=0

while novoGrenal == 1:
    Inter,Gremio=map(int,input().split(" "))
    if Inter > Gremio:
        somaInter += 1
    elif Gremio > Inter:
        somaGremio += 1
    elif Inter == Gremio:
        empate += 1

    somaGrenais += 1
    
    print("Novo grenal (1-sim 2-nao)")
    novoGrenal=int(input())

    if novoGrenal == 2:
        break   

print(somaGrenais,"grenais")
print("Inter:"+(str(somaInter)))
print("Gremio:"+(str(somaGremio)))
print("Empates:"+(str(empate)))
if somaInter > somaGremio:
  print("Inter venceu mais")
elif somaGremio > somaInter:
  print("Gremio venceu mais")
else:
  print("Nao houve vencedor")
