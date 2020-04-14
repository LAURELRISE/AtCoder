N,X,Y=map(int,input().split())
A=[]
for i in range(N-1):
    A.append([-1]*(N-1-i))

Ndmin=[0]*(N-1)
for i in range(N-1):
    for j in range(i+1,N):
        Ndmin[min(j-i,abs(X-i-1)+1+abs(Y-j-1),abs(X-j-1)+1+abs(Y-i-1))-1]+=1

for k in range(N-1):
    print(Ndmin[k])