Q=int(input())
for i in range(Q):
    H,M,O=map(int,input().split())
    if H>9 and M>9:
        if O == 1:
            print(str(H)+":"+str(M),"- A porta abriu!")
        else:
            print(str(H)+":"+str(M),"- A porta fechou!")

    elif H>9 and M<10:
        if O == 1:
            print(str(H)+":0"+str(M),"- A porta abriu!")
        else:
            print(str(H)+":0"+str(M),"- A porta fechou!")

    elif H<10 and M>9:
        if O == 1:
            print("0"+str(H)+":"+str(M),"- A porta abriu!")
        else:
            print("0"+str(H)+":"+str(M),"- A porta fechou!")

    else:
        if O == 1:
            print("0"+str(H)+":0"+str(M),"- A porta abriu!")
        else:
            print("0"+str(H)+":0"+str(M),"- A porta fechou!")
