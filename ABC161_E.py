N,K,C=map(int,input().split())
S=input()

def check0(S0):
    count=0
    index=0
    out=[0]*K
    while count<K and index<N:
        if S0[index]=='o':
            out[count]=index
            count+=1
            index+=(C+1)
        else:
            index+=1
    if count==K:
        return 1,out
    return 0,out

def checkend(S0):
    count=0
    index=N-1
    out=[0]*K
    while count<K and index>=0:
        if S0[index]=='o':
            out[K-1-count]=index
            count+=1
            index-=(C+1)
        else:
            index-=1
    if count==K:
        return 1,out
    return 0,out


flag0,out0=check0(S)
flagend,outend=checkend(S)
if flag0==1:
    for i in range(K):
        if out0[i]==outend[i]:
            print(out0[i]+1)