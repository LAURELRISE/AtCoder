N,A,B=map(int, input().split())

S=A*int(N/(A+B))
if N%(A+B)-A>0:
    S+=A
else:
    S+=N%(A+B)
print(S)