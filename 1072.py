n=int(input())
cont=0
for i in range (0,n):
    x = int(input())
    if x >= 10 and x <= 20:
        cont += 1
print(cont,"in")
print(n-cont,"out")


