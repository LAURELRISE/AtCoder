from collections import deque

# pypy3なら通る
N,X,Y=map(int,input().split())

Ndmin=[0]*(N-1)
for i in range(1,N):# O(N)
    # ベルマン・フォード, ダイクストラではなかった...
    tmp=deque([i])
    dmin=deque([0])
    Dmin=[10000]*(N)
    while tmp:
        E=tmp.popleft()
        d=dmin.popleft()
        Dmin[E-1]=min(d,Dmin[E-1])
        if E<N:# 右隣
            if d+1<Dmin[E]:
                tmp.append(E+1)
                dmin.append(d+1)
        if E>1:# 左隣
            if d+1<Dmin[E-2]:
                tmp.append(E-1)
                dmin.append(d+1)
        if E==X and d+1<Dmin[Y-1]:# X-Y
            tmp.append(Y)
            dmin.append(d+1)
        if E==Y and d+1<Dmin[X-1]:# Y-X
            tmp.append(X)
            dmin.append(d+1)
        
    for ii in range(i,N):
        Ndmin[Dmin[ii]-1]+=1

for i in range(N-1):
    print(Ndmin[i])