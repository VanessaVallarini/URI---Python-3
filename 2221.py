T=int(input())
for i in range(T):
    B=int(input())
    Ad,Dd,Ld=map(int,input().split())
    Ag,Dg,Lg=map(int,input().split())
    Dabriel=(Ad+Dd)/2
    if(Ld%2==0):
        Dabriel += B
    Guarte=(Ag+Dg)/2
    if(Lg%2==0):
        Guarte += B
    if(Dabriel == Guarte):
        print("Empate")
    else:
        if Dabriel > Guarte:
            print("Dabriel")
        else:
            print("Guarte")
