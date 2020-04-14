N=int(input())

S=[input() for _ in range(N)]
S.sort()

label=1
l=1
out=[]
for i in range(N-1):
    if S[i]==S[i+1]:
        l+=1
    else:
        if label<l:
            out=[S[i]]
            label=l
        elif label==l:
            out.append(S[i])
        l=1
if label<l:
    out=[S[-1]]
elif label==l:
    out.append(S[-1])

for i in range(len(out)):
    print(out[i])