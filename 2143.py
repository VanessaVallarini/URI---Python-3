T=1
while T!=0:
    if T==0:
        break
    else:
        T=int(input())
        for i in range(T):
            N=int(input())
            if N%2==0:
                print((N - 2)*2 + 2)
            else:
                print((N - 1)*2 + 1)
