casos = int(input())

while casos > 0:
    
    entrada = input().split()
    PA, PB, G1, G2 = int(entrada[0]), int(entrada[1]), float(entrada[2]), float(entrada[3])
    
    anos = 0
    while PA <= PB:
        PA += int(PA * (G1/100))
        PB += int(PB * (G2/100))
        anos += 1
        if anos > 100:
            print("Mais de 1 seculo.")
            break
    
    if anos <= 100: print("%d anos." % anos)
    
    casos -= 1
    
