while True:
    try:
        h, m = map(int,input().split(':'))
        if h >= 7:
            resultado=m+60*(h-7)
            print("Atraso maximo:",resultado)
        else:
            print("Atraso maximo:",0)
    except EOFError:
        break    

