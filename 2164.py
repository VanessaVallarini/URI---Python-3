import math
N=int(input())
C=(math.pow((1 + math.sqrt(5))/2, N) - math.pow((1 - math.sqrt(5))/2, N))/math.sqrt(5)
print("%.1f" %C)
