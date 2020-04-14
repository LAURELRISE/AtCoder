N,M=map(int,input().split())

flag=True
ex=[False]*(N)
for i in range(M):
    S,C=map(int,input().split())
    if ex[S-1]==False or ex[S-1]==str(C):
        ex[S-1]=str(C)
    else:
        flag=False
        break

if N>1 and ex[0]==str(0):
    flag=False

if flag:
    for i in range(N-1):
        if ex[i+1]==False:
            ex[i+1]='0'
    if ex[0]==False and N>1:
        ex[0]='1'
    elif ex[0]==False:
        ex[0]='0'
    Ex=''.join(ex)
    print(Ex)
else:
    print(-1)