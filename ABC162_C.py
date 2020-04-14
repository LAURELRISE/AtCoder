import math

K=int(input())
out=0
for i in range(1,K+1):
    for ii in range(1,K+1):
        tmp=math.gcd(i,ii)
        for iii in range(1,K+1):
            out+=math.gcd(tmp,iii)

print(out)