x=1
a=0
b=0
soma=0

while x != 0:
    x=int(input())
    soma=0
    a=0
    b=0
    if x == 0:
        break
    elif x%2==0:
        a=x
        b=x+10
        for i in range(a,b,2):
            soma+=i
        
    else:
        a=x+1
        b=x+11
        for i in range(a,b,2):
            soma+=i
            

    print(soma)
