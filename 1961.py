P,N=map(int,input().split())
linha=input().split()
cont=1
for i in range(N-1):
    if int(linha[cont]) > int(linha[i]):
        calculo=(int(linha[cont]) - int(linha[i]))
        if calculo > P:
            resultado="GAME OVER"
            break
        else:
            resultado = "YOU WIN"


    elif int(linha[i]) > int(linha[cont]):
        calculo=(int(linha[i]) - int(linha[cont]))
        if calculo > P:
            resultado="GAME OVER"
            break
        else:
            resultado = "YOU WIN"

    else:
        resultado = "YOU WIN"
    

    cont+=1


print(resultado)
