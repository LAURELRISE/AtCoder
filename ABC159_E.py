from collections import deque

# input
H,W,K=map(int,input().split())
S=[]
for i in range(H):
    S.append(input())

# main
stack=deque([str(1),str(0)])
result=H-1+W-1
while stack:# O(2^H)
    edge=stack.pop()
    if len(edge)<H-1:
        stack.append(edge+str(1))
        stack.append(edge+str(0))
    else:
        ii=0
        for i in range(H-1):
            ii+=int(edge[i])
        Nk=[0]*(ii+1)
        Nw=0
        for iw in range(W):# O(W)
            Nh=0
            Nk0=[0]*(ii+1)
            for ih in range(H-1):# O(H)
                Nk[Nh]+=int(S[ih][iw])
                Nk0[Nh]+=int(S[ih][iw])
                if int(edge[ih])==1:
                    Nh+=1
            Nk[Nh]+=int(S[ih+1][iw])
            Nk0[Nh]+=int(S[ih+1][iw])
            if K<max(Nk):
                Nw+=1
                Nk=Nk0
            elif K<max(Nk0):
                Nh=H-1
                Nw=W-1
                break
        result=min(result,Nh+Nw)
print(result)