qt=int(input())
max=0
for i in range(qt):
    cod,nota=map(float,input().split())
    if nota > max:
        max=nota
        impCod=cod
        impNota=nota

if impNota < 8:
    print("Minimum note not reached")
else:
    print("%0.0f" %impCod)
