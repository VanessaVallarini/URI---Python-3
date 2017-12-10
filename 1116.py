n = int(input())

cont=1

while cont <= n:
    x, y = map(int, input().split(" "))
    if y == 0:
        print("divisao impossivel")
    else:
        print(x/y)
    cont +=1
