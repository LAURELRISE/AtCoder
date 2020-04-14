from collections import deque

K=int(input())
# BFS
M=0
L=9
tmp=deque([1,2,3,4,5,6,7,8,9])
while L<K:
    k=str(tmp.popleft())
    if int(k[-1])-1>=0:
        tmp.append(int(k+str(int(k[-1])-1)))
        L+=1
    tmp.append(int(k+k[-1]))
    L+=1
    if int(k[-1])+1<10:
        tmp.append(int(k+str(int(k[-1])+1)))
        L+=1
    M+=1# 取り出した数

print(tmp[K-1-M])