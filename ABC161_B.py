N,M=map(int,input().split())

A=list(map(int,input().split()))
L=sum(A)
flag=0
for i in range(N):
    if A[i]>=L/(4*M):
        flag+=1

if flag>=M:
    print('Yes')
else:
    print('No')