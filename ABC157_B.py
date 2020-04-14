A=[]
for i in range(3):
    A.append(list(map(int,input().split())))
N=int(input())
for i in range(N):
    b=int(input())
    for ii in range(3):
        for iii in range(3):
            if A[ii][iii]==b:
                A[ii][iii]=0

flag=False
for i in range(3):
    if A[i][:]==[0,0,0]:
        flag=True
    elif A[0][i]==0 and A[1][i]==0 and A[2][i]==0:
        flag=True
    elif A[1][1]==0:
        if A[0][2]==0 and A[2][0]==0:
            flag=True
        elif A[0][0]==0 and A[2][2]==0:
            flag=True
if flag:
    print('Yes')
else:
    print('No')