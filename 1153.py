N = int(input())
cont = 1

if 0 < N < 13:
  for i in range(1, N):
    N = N * cont
    cont+= 1

print(N)
