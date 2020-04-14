N=int(input())
S=input()
R=[]
G=[]
B=[]
for i in range(N):
    if S[i]=='R':
        R.append(i)
    elif S[i]=='G':
        G.append(i)
    else:
        B.append(i)

out=len(R)*len(G)*len(B)
for i in range(N-2):
    for ii in range(1,(N-i)//2+(N-i)%2):
        if S[i]!=S[i+ii] and S[i+ii]!=S[i+2*ii] and S[i]!=S[i+2*ii]:
            out-=1

print(out)