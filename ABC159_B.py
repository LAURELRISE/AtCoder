S=list(input())
N=len(S)

S1=S[:int((N-1)/2)]
S2=S[int((N+3)/2)-1:]
S1r=[i for i in S1[::-1]]
S2r=[i for i in S2[::-1]]
Sr=[i for i in S[::-1]]
if S1==S1r and S2==S2r and S==Sr:
    print('Yes')
else:
    print('No')