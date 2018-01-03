p,j1,j2,r,a=map(int,input().split())

soma=j1+j2

if(soma%2==0 and p==1)or(soma%2!=0 and p==0):
    v=1
else:
    v=2
if((r==1 and a==0) or (r==0 and a==1)):
    v = 1
else:
    if(r==1 and a==1):
        v=2

print("Jogador",v,"ganha!")


