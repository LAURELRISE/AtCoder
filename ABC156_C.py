N=int(input())
X=list(map(int,input().split()))

for i in range(100):
    L0=0
    for ii in range(N):
        L0+=(i+1-X[ii])**2
    
    if i==0:
        L=L0
    else:
        L=min(L,L0)
print(L)