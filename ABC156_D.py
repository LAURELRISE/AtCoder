def powl(x, n, l):#繰り返し2乗法 O(log n)
    ans = 1
    while n > 0:
        if bin(n & 1) == bin(1):
            ans = ans*x
        x = (x*x)%l
        n = n >> 1 #ビットシフト
    return ans

n,a,b=map(int,input().split())

out=powl(2,n,pow(10,9)+7)-1
X,Y=1,1
for i in range(a):
    X=(X*(i+1))%(pow(10,9)+7)
    Y=(Y*(n-i))%(pow(10,9)+7)
out-=Y*powl(X,pow(10,9)+5,pow(10,9)+7)

for i in range(a,b):
    X=(X*(i+1))%(pow(10,9)+7)
    Y=(Y*(n-i))%(pow(10,9)+7)
out-=Y*powl(X,pow(10,9)+5,pow(10,9)+7)

print(out%(pow(10,9)+7))