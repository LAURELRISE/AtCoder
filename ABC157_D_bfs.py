from collections import deque

N,M,K=map(int,input().split())
Sn=[0]*N
Sm=[0]*N
Sk=[0]*N
S=[0]*N

friend=[[] for _ in range(N)]
for i in range(M):#連結数,友達数
    A,B=map(int,input().split())
    Sm[A-1]+=1
    Sm[B-1]+=1
    
    friend[A-1].append(B-1)
    friend[B-1].append(A-1)

label=[-1]*N
for i in range(N):
    if label[i]==-1:
        label[i]=i
        F=deque(friend[i])
        while F:
            F0=F.pop()
            if label[F0]==-1:
                Sn[i]+=1
                label[F0]=i
                for ii in friend[F0]:
                    if label[ii]==-1:
                        F.append(ii)
    else:
        Sn[i]=Sn[label[i]]

for i in range(K):#ブロック数
    C,D=map(int,input().split())
    if label[C-1]==label[D-1]:
        Sk[C-1]+=1
        Sk[D-1]+=1

for i in range(N):
    S[i]=str(Sn[i]-Sm[i]-Sk[i])

print(' '.join(S))