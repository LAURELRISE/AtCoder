N,K=map(int,input().split())

A=list(map(int,input().split()))
A.sort()

Np,Nm,Nz=0,0,0
for i in range(N):
    if A[i]>0:
        Np+=1
    elif A[i]<0:
        Nm+=1
    else:
        Nz+=1

if Np*Nm>=K:
    for i in range(Np):
        A[N-Np]
elif (Np+Nm)*Nz:
    a=1
else:
    a=1