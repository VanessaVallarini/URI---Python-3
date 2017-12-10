tipoCombustivel=1
alcool=0
gasolina=0
diesel=0

while tipoCombustivel != 4:
    tipoCombustivel = int(input())

    if tipoCombustivel == 1:
        alcool += 1
    if tipoCombustivel == 2:
        gasolina += 1
    if tipoCombustivel == 3:
        diesel += 1
    if tipoCombustivel == 4:
        break

print("MUITO OBRIGADO")
print("Alcool:",alcool)
print("Gasolina:",gasolina)
print("Diesel:",diesel)
    



    
