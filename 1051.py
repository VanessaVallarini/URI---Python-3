valor = float(input())


if valor >= 0.00 and valor <= 2000.00:
    print("Isento")
    
elif valor >= 2000.01 and valor <= 3000.00:
    resto= (valor - 2000.00)
    resultato= (resto * 0.08) 
    print("R$ %0.2f" %resultato)

elif valor >= 3001.00 and valor <= 4500.00:
    resto= (valor - 3000.00)
    resultato = (resto * 0.18) + (1000 * 0.08)
    print("R$ %0.2f" %resultato)

if valor > 4500.00:
    resto = valor - 4500
    resultato = (resto * 0.28) + (1500 * 0.18) + (1000 * 0.08)
    print("R$ %0.2f" %resultato)
