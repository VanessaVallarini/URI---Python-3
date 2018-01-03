import math
while True:
    try:
        x1, y1, x2, y2, v, r1, r2 = map(float,input().split())
    except EOFError:
        break
    X = (x2-x1)*(x2-x1)
    Y = (y2-y1)*(y2-y1)
    dstnce = math.sqrt(X+Y)
    dstnce += v*1.50
    r = r1+r2
    if(dstnce > r):
        print("N")
    else:
        print("Y")
