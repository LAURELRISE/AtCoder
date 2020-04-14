N=int(input())
A=list(map(int,input().split()))

for i in range(N):
    A0=A.copy()
    A0.pop(i)
    A0=sorted(A0)
    
    ii=0
    C=0
    L=0
    while ii<N-1:
        C=A0.count(A0[ii])
        ii+=C
        L=int(C*(C-1)/2)+L
    print(L)