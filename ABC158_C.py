A,B=map(int,input().split())
A0=[100*A/8,100*(A+1)/8]
B0=[100*B/10,100*(B+1)/10]
S0=max(A0[0],B0[0])
S1=min(A0[1],B0[1])
if int(S0)>=S0 and int(S0)<S1:
    print(int(S0))
elif int(S0)+1<S1:
    print(int(S0)+1)
else:
    print(-1)