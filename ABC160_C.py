K,N=map(int,input().split())
A=list(map(int,input().split()))

B=sorted(A)
L=0
for i in range(N-1):
    L=max(L,B[i+1]-B[i])
L=max(L,K+B[0]-B[N-1])
print(K-L)