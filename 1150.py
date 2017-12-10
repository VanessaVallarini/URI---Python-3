x=int(input())
z=int(input())

soma=0
cont=0

while z <= x:
    z=int(input())

if  z > x:
    for i in range(x,z):
        soma += i
        cont += 1
        if soma >= z:
            break
    
print(cont)
