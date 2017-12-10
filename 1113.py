x=0
y=1

while x != y:
    x, y = map(int, input().split())

    if (x<y):
      print("Crescente")

    elif (y<x):
        print("Decrescente")

    else:
        break
