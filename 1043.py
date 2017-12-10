line = input().split()

a = float(line[0])
b = float(line[1])
c = float(line[2])

if((a<(b+c)) and (b<(a+c)) and (c<(a+b))):
    p=a+b+c
    print("Perimetro =", p)
else:
    area=((a+b)/2)*c
    print("Area =", area)
    
