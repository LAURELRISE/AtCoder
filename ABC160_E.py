X,Y,A,B,C=map(int,input().split())
P=list(map(int,input().split()))
Q=list(map(int,input().split()))
R=list(map(int,input().split()))

P.sort(reverse=1)
Q.sort(reverse=1)
R.sort(reverse=1)

R0=P[:X]
R0.extend(Q[:Y])
R0.sort()
for i in range(C):
    if R0[i]<R[i]:
        R0[i]=R[i]
    else:
        break
print(sum(R0))