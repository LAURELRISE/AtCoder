N=int(input())
out=0
for i in range(1,N+1):
    if i%3 and i%5:
        out+=i

print(out)