n = int(input())
a = 1
if 1 < n < 1000:
  for i in range(0,n):
    print(a,a**2,a**3)
    print(a,a**2+1,a**3+1)
    a+=1   
