while True:
    try:
        d=0.0
        e=0.0
        f=0.0
        x=0
        M=int(input())
        for i in range(M):
            N,C=map(int,input().split())
            d+=N*C
            e+=C
        x=(float(d/e))/100
        print("%.4f" %x)
        
    except EOFError:
        break
    
