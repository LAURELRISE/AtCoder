N,K,C=map(int,input().split())
S=input()

def check(S0):
    count=0
    index=0
    while count<K and index<N:
        if S0[index]=='o':
            count+=1
            index+=(C+1)
        else:
            index+=1
    if count==K:
        return 1
    return 0

if check(S)==0:
    print()
else:
    for i in range(N):#O(N^2)よりTLE
        if S[i]=='o':
            S0=S[:i]+'x'+S[i+1:]
            if check(S0)==0:
                print(i+1)