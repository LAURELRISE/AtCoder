N,K=map(int,input().split())

if K-N%K>N%K:
    print(N%K)
else:
    print(K-N%K)