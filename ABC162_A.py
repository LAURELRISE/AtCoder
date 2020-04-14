N=int(input())

label=0
N1=N//100
N2=(N-N1*100)//10
N3=(N-N1*100-N2*10)

if N1==7 or N2==7 or N3==7:
    print('Yes')
else:
    print('No')