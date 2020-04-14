A,B,C=map(int,input().split())

out=0
if A==B:
    out+=1
if B==C:
    out+=1
if A==C:
    out+=1

if out==1:
    print('Yes')
else:
    print('No')